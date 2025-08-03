import streamlit as st

st.title("Hello to All of them!!!")
st.subheader("Brewed with streamlit")
st.text("Welcome to first interactive app")
st.write("Select your fav. icecreamuv ")

icecream = st.selectbox("your fav ice-cream",["chocolate ice-cream","Butterscoh ice-cream","cookiencream ice-cream"])
st.write(f"You have selected {icecream}")
st.success("your icecream is ready!!")