import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from datetime import timedelta

def CreateChart(data,reading,option):
    now = pd.Timestamp.now(tz="Asia/Kolkata")
    
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
    st.line_chart(filtered.set_index("timestamp")[reading])

def AnalyticsPage():

    st.title("Analytics")
    st.text("Work is not completed for this page.")
    response = requests.get("https://apiforsmartplanter.onrender.com/history")
    data = pd.DataFrame(response.json())

    data["timestamp"] = pd.to_datetime(data["timestamp"],  format="ISO8601")

        
    with st.expander("📊 Show Historical Data"):
        display_data = data.copy()

        display_data["timestamp"] = (
        display_data["timestamp"].dt.strftime("%d-%m-%Y %H:%M"))
        st.dataframe(data)

    with st.expander("Show Moisture Trend"):
        
        option_m = st.selectbox(
    "Select Time Range",
    [
        "24 Hours",
        "7 Days",
        "30 Days"
    ], key = 1
)
        CreateChart(data,"moisture",option_m)
    
    with st.expander("Show pH Trend"):
        
         option_p = st.selectbox(
    "Select Time Range",
    [
        "24 Hours",
        "7 Days",
        "30 Days"
    ],key= 2)
         CreateChart(data,"ph",option_p)