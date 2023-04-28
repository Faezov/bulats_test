import streamlit as st
import requests

st.title("bulats_model")

user_input = st.text_area("Enter data for prediction:", "")

if st.button("Predict"):
    response = requests.post("https://your-fastapi-app-url/predict/", data=user_input)
    prediction = response.json()["prediction"]
    
    st.write(f"Prediction: {prediction}")
