import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('titanic_model.pkl')

# Create a Streamlit web application
st.title('Titanic Survival Prediction')

# Input form for passenger details
st.write('Enter Passenger Details:')
Pclass = st.selectbox('Pclass', [1, 2, 3])
Sex = st.selectbox('Sex', ['male', 'female'])
Age = st.slider('Age', 0, 100, 30)
SibSp = st.number_input('SibSp', min_value=0, max_value=10, value=0)
Parch = st.number_input('Parch', min_value=0, max_value=10, value=0)
Fare = st.number_input('Fare', min_value=0.0, value=50.0)
Embarked_Q = 1 if st.selectbox('Embarked_Q', ['Yes', 'No']) == 'Yes' else 0
Embarked_S = 1 if st.selectbox('Embarked_S', ['Yes', 'No']) == 'Yes' else 0

# Make prediction based on input values
input_data = [[Pclass, 1 if Sex == 'male' else 0, Age, SibSp, Parch, Fare, Embarked_Q, Embarked_S]]
prediction = model.predict(input_data)

if st.button('Predict'):
    if prediction[0] == 1:
        st.write('The passenger is likely to survive.')
    else:
        st.write('The passenger is unlikely to survive.')