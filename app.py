import streamlit as st

from streamlit_option_menu import (
    option_menu
)

from streamlit_firebase_auth import FirebaseAuth

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
# FIREBASE CONFIG
# -----------------------------

config = {

    "apiKey": "AIzaSyAQfWHn-PfdwL-Z2C7T2LFWm4L7uLX7bB8",

    "authDomain": "smart-planter-a00a0.firebaseapp.com",

    "projectId": "smart-planter-a00a0",

    "storageBucket": "smart-planter-a00a0.firebasestorage.app",

    "messagingSenderId": "1076034199324",

    "appId": "1:1076034199324:web:0ecb27cb7a81295cec24d9",

    "measurementId": "G-QKNV76E891"

}

# -----------------------------
# AUTHENTICATION
# -----------------------------

authenticator = FirebaseAuth(config)

user = authenticator.login()

# -----------------------------
# LOGIN CHECK
# -----------------------------

if not user:

    st.warning(
        "Please login to continue"
    )

    st.stop()

# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title(
        "🌱 Smart Planter"
    )

    st.success(
        f"Logged in as\n{user['email']}"
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
        "STEM Prototype v2.1"
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