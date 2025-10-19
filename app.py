
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("model-reg-67130701921.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit app title
st.title("Advertising Sales Predictor")

# User input fields
youtube = st.number_input("YouTube Advertising Budget", min_value=0.0, value=50.0)
tiktok = st.number_input("TikTok Advertising Budget", min_value=0.0, value=50.0)
instagram = st.number_input("Instagram Advertising Budget", min_value=0.0, value=50.0)

# Predict button
if st.button("Predict Sales"):
    # Create a DataFrame from user input
    input_data = pd.DataFrame({
        "youtube": [youtube],
        "tiktok": [tiktok],
        "instagram": [instagram]
    })

    # Make prediction
    prediction = model.predict(input_data)

    # Show result
    st.success(f"Estimated Sales: {prediction[0]:.2f}")
