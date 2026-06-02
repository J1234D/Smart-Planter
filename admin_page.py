import streamlit as st
from firebase_admin import auth as admin_auth

def AdminPage():

    st.title("🛡 Admin Panel")

    st.subheader(
        "System Controls"
    )

    st.success(
        "Admin access granted"
    )

    users = admin_auth.list_users()

    count = 0
    
    for user in users.users:
        count+=1

    st.metric(
    "👥 Total Users",
    count
    )