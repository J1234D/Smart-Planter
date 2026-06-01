import streamlit as st
from datetime import datetime
from streamlit_autorefresh import (
    st_autorefresh
)

import requests
import pandas as pd

from rules import get_plant_status


def DashPage():

    # -----------------------------
    # AUTO REFRESH
    # -----------------------------

    st_autorefresh(
        interval=5000,
        key="refresh"
    )

    # -----------------------------
    # LOAD LIVE DATA
    # -----------------------------

    headers = {
    "x-api-key": st.secrets["API_KEY"]
}
    
    response = requests.get(
        "https://apiforsmartplanter.onrender.com/sensor_readings",
        headers=headers
    )

    live_data = response.json()

    data = pd.DataFrame(
        live_data.values()
    )

    # -----------------------------
    # TIMESTAMP
    # -----------------------------

    data["timestamp"] = pd.to_datetime(
        data["timestamp"],
        format="ISO8601"
    )

    # -----------------------------
    # PLANT LABELS
    # -----------------------------

    plant_info = (

        data[
            ["plant_id", "plant_type"]
        ]

        .drop_duplicates()

    )

    plant_labels = {

        row["plant_id"]:

        f"Plant {row['plant_id']} - "
        f"{row['plant_type'].title()}"

        for _, row in plant_info.iterrows()

    }

    # -----------------------------
    # SELECT PLANT
    # -----------------------------

    selected_plant = st.selectbox(

        "🌱 Select Plant",

        data["plant_id"].unique(),

        format_func=lambda x:
            plant_labels.get(x, x)

    )

    # -----------------------------
    # FILTER PLANT
    # -----------------------------

    plant_data = data[
        data["plant_id"]
        == selected_plant
    ]

    latest = plant_data.iloc[0]

    # -----------------------------
    # STATUS
    # -----------------------------

    status = get_plant_status(

        latest["plant_type"],

        latest["moisture"],

        latest["ph"]

    )

    # -----------------------------
    # UI
    # -----------------------------

    st.title(
        "🌱 Smart Planter Dashboard"
    )

    current_time = latest["timestamp"]

    st.caption(

        "Last Updated: "

        + current_time.strftime(
            "%H:%M:%S"
        )

    )

    # -----------------------------
    # METRICS
    # -----------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "💧 Moisture",

            f"{latest['moisture']}%"

        )

    with col2:

        st.metric(

            "🧪 pH",

            latest["ph"]

        )

    with col3:

        st.metric(

            "☀ Light Status",

            "☀ Day"

            if latest["is_day"]

            else "🌙 Night"

        )

    st.divider()

    # -----------------------------
    # STATUS DISPLAY
    # -----------------------------

    st.subheader(
        "Plant Status"
    )

    for issue in status:

        if "Healthy" in issue:

            st.success(issue)

        elif "Needs Water" in issue:

            st.error(issue)

        else:

            st.warning(issue)