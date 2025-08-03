import streamlit as st 

st.title("Ice-cream Shop")
if st.button("Order Ice-cream"):
    st.success("Your icecream is ready")

add_chocochips = st.checkbox("Add chocochips!")

if add_chocochips:
    st.write("Added chocochips")

tea_flavor = st.radio("Pick your flavor:",["butterscoh","chocolate","cookiencream"])
st.write(f"You selected {tea_flavor}")

chocochips = st.slider("No. of spoon chocochips",0,5,2)
st.write(f"You selected No. of chocochips {chocochips}")

cups = st.number_input("No. of cups:",min_value = 1,max_value = 10 , step = 1)

name = st.text_input("Enter your name")
st.write(f"your name is {name}")

dob = st.date_input("Select your date of birth")
st.write(f"your dob is {dob}")

