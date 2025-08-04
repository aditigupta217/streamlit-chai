import streamlit as st 
import pandas as pd

st.title("Practice!!")

file = st.file_uploader("upload your csv or xlsx file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("previwe file")
    st.dataframe(df)

