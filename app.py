from streamlit_autorefresh import st_autorefresh
import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

from sensors import get_sensor_data
from rules import get_plant_status

# Refresh every 5 seconds
st_autorefresh(interval=5000, key="refresh")

st.set_page_config(
    page_title="Smart Planter",
    page_icon="🌱",
    layout="wide"
)


data = get_sensor_data()

status = get_plant_status(
    data["moisture"],
    data["ph"]
)


with st.sidebar :
    selected = option_menu(
        menu_title="Main Menu",
        options=["Dashboard","Analytics","About"]
    )

if selected == "Dashboard":
    
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

if selected == "Analytics":

    st.title("Analytics")

if selected == "About":

    st.title("About")