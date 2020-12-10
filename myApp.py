import streamlit as st


st.write("Get sentiment of FX pairs")


user_input = st.text_input("What currency pair are you looking at?", "EURUSD")

sentimentScore = st.slider("select a number") 
st.write("You chose", sentimentScore)
