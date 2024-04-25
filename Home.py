import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title= "Home",
                   page_icon=":bar_chart:",
                   layout="wide")



st.title("Solar Radiation Measurement Data")
st.cache_data
def load_data(path:str):
    data=pd.read_csv(path)
    return data



with st.sidebar:
    upload_file= st.file_uploader("choose a file",type=["csv", "xlsx"])
    if upload_file is None:
        st.info("upload file through config ")
        st.stop()

df=load_data(upload_file)
col1, col2, col3= st.columns([1,1,1])
with col1.expander("srm data"):
    st.dataframe(
        df,
        column_config={
            "Year":st._column_config.NumberColumn(format="%d")

        }
    )

info= df.describe()
with col2.expander("description"):
    st.write(info)

#scatter
st.cache_data
def scatter_plot():
    fig =px.scatter(df,x="Timestamp",y="DNI",title="Timestamps of DNI") 
    st.plotly_chart(fig,use_container_width=True)

with col1:
    scatter_plot()  
def line_plot():
    fig =px.line(df,x="Timestamp",y="DNI",text=" DNI",markers=True) 
    st.plotly_chart(fig,use_container_width=True)

with col2:
    line_plot()  
