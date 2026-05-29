import streamlit as st
from datetime import datetime
from sensors import get_sensor_data
from rules import get_plant_status


def DashPage():
    
    data = get_sensor_data()

    status = get_plant_status(
    data["moisture"],
    data["ph"]
)

    st.title("🌱 Smart Planter Dashboard")
    st.caption(
    f"Last Updated: {datetime.now().strftime('%H:%M:%S')}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Moisture", f"{data['moisture']}%")

    with col2:
        st.metric("pH", data["ph"])

    with col3:
        st.metric("Temperature", f"{data['temperature']}°C")

    st.divider()

    st.subheader("Plant Status")

    for issue in status:
        if "Healthy" in issue:
            st.success(issue)
            
        elif "Needs Water" in issue:
            st.error(issue)

        else:
            st.warning(issue)