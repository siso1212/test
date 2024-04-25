import streamlit as st

st.set_page_config(page_title= "basics",
                   page_icon=":bar_chart:",
                   layout="wide")

st.title("EDA Analysis Results")
val= st.slider("Selet a value",0,100,50,step=10)
st.write(val)