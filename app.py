from streamlit_autorefresh import st_autorefresh
import streamlit as st
from streamlit_option_menu import option_menu

from dashboard_page import DashPage
from analytics_page import AnalyticsPage
from about_page import AboutPage


# Refresh every 5 seconds
st_autorefresh(interval=5000, key="refresh")

st.set_page_config(
    page_title="Smart Planter",
    page_icon="🌱",
    layout="wide"
)



with st.sidebar :
    selected = option_menu(
        menu_title="Main Menu",
        options=["Dashboard","Analytics","About"]
    )

if selected == "Dashboard":
    
    DashPage()
   
if selected == "Analytics":

    AnalyticsPage()

if selected == "About":

    AboutPage()