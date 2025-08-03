import streamlit as st 

st.title("Our Ice-cream")

col1, col2 = st.columns(2)

with col1:
    st.header("Pista Icecream")
    vote1 = st.button("vote pista icecream")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGtKAkNr-vD5fJMVCnm-6Bu1IBf4z2VLEw3w&s",width=200)
with col2:
     st.header("Vanila Icecream")
     vote2 = st.button("vote Vanila icecream")
     st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMWXTQkjsODxer3INa63_3Il-3WxOVGxTv9Q&s",width = 200)

if vote1:
     st.success("YOu vote pista icecream")
elif vote2:
     st.success("you vote vanila icecream")

name = st.sidebar.text_input("Enter YOur Name")
icecream = st.sidebar.selectbox("Select flavor:",["chocolate","butterscoh","cookiencream"])
st.write(f"Hello {name}, Your flavor is {icecream}")

with st.expander("The Rule are:"):
     st.write("""
     1. Non-Cancelable
     2. No exchange
     3. Money First
 """)
     
st.markdown('### Welcome to Ice-cream Appp')
st.markdown()
     
