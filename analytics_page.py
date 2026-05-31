import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from datetime import timedelta

def AnalyticsPage():

    st.title("Analytics")
    st.text("Work is not completed for this page.")
    response = requests.get("https://apiforsmartplanter.onrender.com/history")
    data = pd.DataFrame(response.json())
        
    with st.expander("📊 Show Historical Data"):
        st.dataframe(data)

    data["timestamp"] = pd.to_datetime(data["timestamp"],  format="ISO8601")

    with st.expander("Show Moisture Trend"):
        
        now = pd.Timestamp.now(tz="Asia/Kolkata")
        option = st.selectbox(
    "Select Time Range",
    [
        "24 Hours",
        "7 Days",
        "30 Days"
    ]
)
        if option == "24 Hours":
            filtered = data[
        data["timestamp"] >= now - timedelta(hours=24)
    ]

        elif option == "7 Days":
            filtered = data[
        data["timestamp"] >= now - timedelta(days=7)
    ]

        elif option == "30 Days":
            filtered = data[
        data["timestamp"] >= now - timedelta(days=30)
    ]
        st.line_chart(filtered.set_index("timestamp")["moisture"])