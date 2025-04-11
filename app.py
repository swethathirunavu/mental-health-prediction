import streamlit as st
import pandas as pd
from predictor import predict_mental_health
from chatbot import get_chatbot_response

st.set_page_config(page_title="Teen Mental Health Support", layout="centered")

st.title("🧠 Teen Mental Health Predictor & Support")

# Input form
st.header("📋 Enter Your Details")

name = st.text_input("Name")
age = st.slider("Age", 10, 25, 16)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
anxiety = st.slider("Anxiety Level", 0, 10, 5)
depression = st.slider("Depression Level", 0, 10, 5)
stress = st.slider("Stress Level", 0, 10, 5)
bullying = st.selectbox("Experienced Bullying?", ["Yes", "No"])
sleep = st.slider("Average Sleep (hrs)", 0, 12, 6)

if st.button("Predict Mental Health"):
    result = predict_mental_health(age, gender, anxiety, depression, stress, bullying, sleep)
    
    st.subheader("🔮 Prediction Result:")
    st.write(f"**{name}**, your mental health condition is likely: **{result}**")

    st.subheader("💡 Suggestions:")
    st.write(get_chatbot_response(result))

st.markdown("---")
st.subheader("💬 Feeling low? Talk to our friendly bot:")

user_input = st.text_input("Say something to the bot 👇")

if user_input:
    response = get_chatbot_response(user_input)
    st.text_area("Bot:", value=response, height=100)
