# import required libraries
import streamlit as st  # for creating web ui
import pickle # to load saved model

# load the trained model from file
model=pickle.load(open('model.pkl','rb'))

# set title of the web app
st.title("Salary Prediction App")

# create input field for user to enter experience
exp=st.number_input("enter experience",min_value=0,max_value=50,value=1)

# create a button when clicked,prediction will run
if st.button("Predict"):
    
    # model expects input in 2D format [[value]]
    result=model.predict([[exp]])
    
    #display the predicted salary on screen
    st.write(f"Predicted Salary: {int(result[0])}")
    
    