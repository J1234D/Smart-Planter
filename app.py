import streamlit as st
import pyrebase

from streamlit_option_menu import (
    option_menu
)

from dashboard_page import DashPage
from analytics_page import AnalyticsPage
from about_page import AboutPage

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(

    page_title="Smart Planter",

    page_icon="🌱",

    layout="wide"

)

# -----------------------------------
# FIREBASE CONFIG
# -----------------------------------

config = {

    "apiKey": "AIzaSyAQfWHn-PfdwL-Z2C7T2LFWm4L7uLX7bB8",

    "authDomain": "smart-planter-a00a0.firebaseapp.com",

    "projectId": "smart-planter-a00a0",

    "storageBucket": "smart-planter-a00a0.firebasestorage.app",

    "messagingSenderId": "1076034199324",

    "appId": "1:1076034199324:web:0ecb27cb7a81295cec24d9",

    "databaseURL": ""

}

# -----------------------------------
# FIREBASE INIT
# -----------------------------------

firebase = pyrebase.initialize_app(
    config
)

auth = firebase.auth()

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "user" not in st.session_state:

    st.session_state.user = None

# -----------------------------------
# LOGIN PAGE
# -----------------------------------

if st.session_state.user is None:

    st.title("🌱 Smart Planter Login")

    auth_mode = st.radio(

        "Select Option",

        [
            "Login",
            "Sign Up"
        ]

    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(

        "Password",

        type="password"

    )

    # -----------------------------
    # LOGIN
    # -----------------------------

    if auth_mode == "Login":

        if st.button("Login"):

            try:

                user = auth.sign_in_with_email_and_password(

                    email,

                    password

                )

                st.session_state.user = user

                st.rerun()

            except Exception as e:

                 st.error(e)

    # -----------------------------
    # SIGN UP
    # -----------------------------

    else:

        if st.button("Create Account"):

            try:

                auth.create_user_with_email_and_password(

                    email,

                    password

                )

                st.success(
                    "Account created successfully! Now please log in."
                )

            except Exception as e:

                 st.error(e)

    st.stop()

ADMIN_EMAILS = [
    
"jishnudutta2002@gmail.com"

]

# -----------------------------------
# ADMIN CHECK
# -----------------------------------

is_admin = False

if st.session_state.user is not None:
    is_admin = (
        st.session_state.user["email"]
        in ADMIN_EMAILS
    )

# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:

    st.title(
        "🌱 Smart Planter"
    )

    st.success(
        f"User: {st.session_state.user['email']}"
    )

    if st.button("Logout"):

        st.session_state.user = None

        st.rerun()

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

# -----------------------------------
# NAVIGATION
# -----------------------------------

if selected == "Dashboard":

    DashPage()

elif selected == "Analytics":

    AnalyticsPage()

elif selected == "About":

    AboutPage()