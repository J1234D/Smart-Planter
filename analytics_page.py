import streamlit as st
import requests

def AnalyticsPage():

    st.title("Analytics")
    st.text("Work is not completed for this page.")
    response = requests.get("https://apiforsmartplanter.onrender.com/history")
    data = response.json()
        
    if "show_table" not in st.session_state:
        st.session_state.show_table = False

    if st.button("Show Data"):
        st.session_state.show_table = True

    if st.button("Close"):
        st.session_state.show_table = False

    if st.session_state.show_table:
        st.dataframe(data)