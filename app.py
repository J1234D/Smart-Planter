import streamlit as st

from streamlit_option_menu import (
    option_menu
)

from dashboard_page import DashPage
from analytics_page import AnalyticsPage
from about_page import AboutPage


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(

    page_title="Smart Planter",

    page_icon="🌱",

    layout="wide"

)


# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title(
        "🌱 Smart Planter"
    )

    selected = option_menu(

        menu_title="Main Menu",

        options=[
            "Dashboard",
            "Analytics",
            "About"
        ],

        icons=[
            "speedometer2",
            "graph-up",
            "info-circle"
        ],

        default_index=0

    )

    st.caption(
        "STEM Prototype v1.0"
    )


# -----------------------------
# NAVIGATION
# -----------------------------

if selected == "Dashboard":

    DashPage()

elif selected == "Analytics":

    AnalyticsPage()

elif selected == "About":

    AboutPage()