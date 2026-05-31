import streamlit as st
import requests

def AnalyticsPage():

    st.title("Analytics")
    st.text("Work is not completed for this page.")
    response = requests.get("https://apiforsmartplanter.onrender.com/history")
    data = response.json()
        
    with st.expander("📊 Show Historical Data"):
        st.dataframe(data)