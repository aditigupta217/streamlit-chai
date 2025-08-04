import streamlit as st 
import requests

st.title("Welcomee! to live currency converter")
amount = st.number_input("Enter the amount in INR",min_value = 1)

target_currency = st.selectbox("Conver to:",["USD","EUR","GBP", "JPY"])

if st.button("convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

