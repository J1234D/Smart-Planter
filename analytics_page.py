import streamlit as st
import requests
import pandas as pd
from datetime import datetime
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh


@st.cache_data(ttl=30)
def load_data():
    response = requests.get(
        "https://apiforsmartplanter.onrender.com/history"
    )

    data = pd.DataFrame(response.json())

    data["timestamp"] = pd.to_datetime(
        data["timestamp"],
        format="ISO8601"
    )

    return data


def CreateChart(data,reading,option):
    now = pd.Timestamp.now(tz="Asia/Kolkata")
    data = data.sort_values("timestamp")
    
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

def ShowTrend(data, title, reading, key):
    with st.expander(title):

        option = st.selectbox(
            "Select Time Range",
            ["24 Hours", "7 Days", "30 Days"],
            key=key
        )

        CreateChart(data, reading, option)

def AnalyticsPage():


    st_autorefresh(interval=10000, key="analytics_refresh")
    st.title("Analytics")
    st.text("Work is not completed for this page.")
    data = load_data()

        
    with st.expander("📊 Show Historical Data"):
        display_data = data.copy()

        display_data["timestamp"] = (
        display_data["timestamp"].dt.strftime("%d-%m-%Y %H:%M"))
        st.dataframe(display_data)

    ShowTrend(data, "Show Moisture Trend", "moisture", 1)
    ShowTrend(data, "Show pH Trend", "ph", 2)