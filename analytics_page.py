import streamlit as st
import requests
import pandas as pd
from datetime import timedelta
from streamlit_autorefresh import st_autorefresh


# -----------------------------
# LOAD DATA
# -----------------------------

@st.cache_data(ttl=10)
def load_data():

    try:
        headers = {"x-api-key": st.secrets["API_KEY"]}

        response = requests.get(
            "https://apiforsmartplanter.onrender.com/history",headers=headers
        )

        response.raise_for_status()

        data = pd.DataFrame(response.json())

        data["timestamp"] = pd.to_datetime(
            data["timestamp"],
            format="ISO8601"
        )

        return data

    except Exception as e:

        st.error(e)

        return None


# -----------------------------
# CREATE CHART
# -----------------------------

def CreateChart(data, reading, option):

    now = pd.Timestamp.now(
        tz="Asia/Kolkata"
    )

    data = data.sort_values(
        "timestamp"
    )

    if option == "24 Hours":

        filtered = data[
            data["timestamp"]
            >= now - timedelta(hours=24)
        ]

    elif option == "7 Days":

        filtered = data[
            data["timestamp"]
            >= now - timedelta(days=7)
        ]

    elif option == "30 Days":

        filtered = data[
            data["timestamp"]
            >= now - timedelta(days=30)
        ]

    st.line_chart(
        filtered.set_index("timestamp")[reading]
    )


# -----------------------------
# TREND SECTION
# -----------------------------

def ShowTrend(data, title, reading, key):

    with st.expander(title, expanded=False):

        option = st.selectbox(

            "Select Time Range",

            [
                "24 Hours",
                "7 Days",
                "30 Days"
            ],

            key=key

        )

        CreateChart(
            data,
            reading,
            option
        )


# -----------------------------
# ANALYTICS PAGE
# -----------------------------

def AnalyticsPage():

    st_autorefresh(
        interval=10000,
        key="analytics_refresh"
    )

    st.title("📈 Smart Planter Analytics")

    st.caption(
        "Historical trends and plant monitoring"
    )

    data = load_data()

    if data is None:

        st.error(
            "Failed to load data from API."
        )

        return

    # -----------------------------
    # PLANT SELECTOR
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

    selected_plant = st.selectbox(

        "🌱 Select Plant",

        data["plant_id"].unique(),

        format_func=lambda x:
            plant_labels.get(x, x)

    )

    # -----------------------------
    # FILTER PLANT DATA
    # -----------------------------

    plant_data = data[
        data["plant_id"]
        == selected_plant
    ]

    # -----------------------------
# AVERAGE METRICS
# -----------------------------

    avg_moisture = (
        plant_data["moisture"]
        .mean()
    )

    avg_ph = (
        plant_data["ph"]
        .mean()
    )

    day_percentage = (

        plant_data["is_day"]
        .mean()

        * 100

    )

    st.subheader(
        f"🌿 {plant_data.iloc[-1]['plant_type'].title()}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "💧 Avg Moisture",

            f"{avg_moisture:.1f}%"

        )

    with col2:

        st.metric(

            "🧪 Avg pH",

            f"{avg_ph:.1f}"

        )

    with col3:

        st.metric(

            "☀ Day Time",

            f"{day_percentage:.0f}%"

    )
    st.divider()

    # -----------------------------
    # HISTORICAL TABLE
    # -----------------------------

    with st.expander(
        "📊 Show Historical Data"
    ):

        display_data = (
            plant_data.copy()
        )

        display_data["timestamp"] = (

            display_data["timestamp"]

            .dt.strftime(
                "%d-%m-%Y %H:%M"
            )

        )

        st.dataframe(

            display_data,

            use_container_width=True

        )

    # -----------------------------
    # CHARTS
    # -----------------------------

    ShowTrend(

        plant_data,

        "💧 Moisture Trend",

        "moisture",

        "moisture_chart"

    )

    ShowTrend(

        plant_data,

        "🧪 pH Trend",

        "ph",

        "ph_chart"

    )