import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
from zoneinfo import ZoneInfo
import requests
from rules import get_plant_status


def DashPage():
    
    # Refresh every 5 seconds
    st_autorefresh(interval=5000, key="refresh")

    response = requests.get("https://apiforsmartplanter.onrender.com/sensor_readings")
    data = response.json()
    st.write(data)

    status = get_plant_status(
    data["moisture"],
    data["ph"]
)

    st.title("🌱 Smart Planter Dashboard")

    """current_time = datetime.now(
    ZoneInfo("Asia/Kolkata")
)"""
    current_time = datetime.fromisoformat(
    data["timestamp"]
)
    st.caption(
    f"Last Updated: {current_time.strftime('%H:%M:%S')}"
)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Moisture", f"{data['moisture']}%")

    with col2:
        st.metric("pH", data["ph"])
    
    with col3:
        st.metric(
        "☀ Light Status",
        "☀ Day" if data["is_day"] else "🌙 Night"
        )
    st.divider()

    st.subheader("Plant Status")

    for issue in status:
        if "Healthy" in issue:
            st.success(issue)
            
        elif "Needs Water" in issue:
            st.error(issue)

        else:
            st.warning(issue)
