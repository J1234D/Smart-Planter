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
    st.write(users)

    count = 0
    user_data = []
    
    for user in users.users:
        count+=1
        user_data.append({

        "Email": user.email,

        "UID": user.uid,

        "Disabled": user.disabled

    })

    st.metric(
    "👥 Total Users",
    count
    )
    st.dataframe(
    user_data,
    use_container_width=True
    )