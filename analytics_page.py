import streamlit as st
import requests
import pandas as pd
from datetime import datetime

def AnalyticsPage():

    st.title("Analytics")
    st.text("Work is not completed for this page.")
    response = requests.get("https://apiforsmartplanter.onrender.com/history")
    data = pd.DataFrame(response.json())
        
    with st.expander("📊 Show Historical Data"):
        st.dataframe(data)

    data["timestamp"] = pd.to_datetime(data["timestamp"],  format="ISO8601")

    with st.expander("Show Moisture Trend"):
        st.line_chart(
            data=data,
            x="timestamp",
            y="moisture"
        )