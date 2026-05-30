import streamlit as st
import requests

def AnalyticsPage():

    st.title("Analytics")
    response = requests.get("https://apiforsmartplanter.onrender.com/history")
    data = response.json()
    st.dataframe(data)