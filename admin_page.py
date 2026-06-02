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

    if st.button("🔄 Refresh Users"):

        st.rerun()

    users = admin_auth.list_users()

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

    st.subheader(
    "🔒 Disable User"
    )

    selected_email = st.selectbox(

        "Select User Email",

        [user["Email"] for user in user_data]

    )

    if st.button("Disable User"):

        admin_auth.update_user(

            selected_email,

            disabled=True

        )

        st.success(
            "User disabled successfully"
        )
    if st.button("Enable User"):

        user_record = admin_auth.get_user_by_email(
        selected_email
        )

        admin_auth.update_user(

        user_record.uid,

        disabled=False

        )

        st.success(
        "User enabled successfully"
        )