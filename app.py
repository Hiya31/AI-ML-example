from flask import Flask,request,jsonify
# flask for api,request for input,jsonify for output
import pickle
# to load saved model

# create flask app
app=Flask(__name__)
# load the trained model from model.pkl file
model=pickle.load(open('model.pkl','rb'))

# home route(juts check if API is running)
@app.route('/')
def home():
    return "API Running!"

# Prediction route(main functionality)
@app.route('/predict',methods=['POST'])
def predict():
     # get data from request(JSON format)
     data=request.json
     
     # extract 'experience' value from input
     exp=data['experience']
     
     # predict salary using model
     #model expects input in 2D format 
     # [[value]]
     result=model.predict([[exp]])
     
     #return result as JSON response
     return jsonify({
         "salary":int(result[0]) # convert prediction to 
     })
     
# run the app
if __name__=='__main__':
    app.run(debug=True) # debug=True helps in development