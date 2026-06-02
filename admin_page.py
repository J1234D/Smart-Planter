import streamlit as st
import requests
from firebase_admin import auth as admin_auth


def AdminPage(ADMIN_EMAILS):

    st.title("🛡 Admin Panel")

    st.subheader(
        "System Controls"
    )

    st.success(
        "Admin access granted"
    )

    # -----------------------------------
    # TABS
    # -----------------------------------

    tab1, tab2 = st.tabs([

        "👥 Users",

        "📊 System"

    ])

    # ===================================
    # USERS TAB
    # ===================================

    with tab1:

        # -----------------------------
        # REFRESH
        # -----------------------------

        if st.button("🔄 Refresh Users"):

            st.rerun()

        # -----------------------------
        # LOAD USERS
        # -----------------------------

        users = admin_auth.list_users()

        count = 0

        user_data = []

        for user in users.users:

            count += 1

            user_data.append({

                "Email": user.email,

                "UID": user.uid,

                "Disabled": user.disabled

            })

        # -----------------------------
        # METRICS + TABLE
        # -----------------------------

        st.metric(

            "👥 Total Users",

            count

        )

        st.dataframe(

            user_data,

            use_container_width=True

        )

        # -----------------------------
        # USER SELECTOR
        # -----------------------------

        st.subheader(
            "👤 User Controls"
        )

        selected_email = st.selectbox(

            "Select User Email",

            [user["Email"] for user in user_data]

        )

        # -----------------------------
        # DISABLE USER
        # -----------------------------

        if st.button("Disable User"):

            if selected_email in ADMIN_EMAILS:

                st.error(
                    "Admin accounts cannot be disabled"
                )

                st.stop()

            user_record = admin_auth.get_user_by_email(
                selected_email
            )

            admin_auth.update_user(

                user_record.uid,

                disabled=True

            )

            st.success(
                "User disabled successfully"
            )

            st.rerun()

        # -----------------------------
        # ENABLE USER
        # -----------------------------

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

            st.rerun()

        # -----------------------------
        # DELETE USER
        # -----------------------------

        if st.button("🗑 Delete User"):

            if selected_email in ADMIN_EMAILS:

                st.error(
                    "Admin accounts cannot be deleted"
                )

                st.stop()

            user_record = admin_auth.get_user_by_email(
                selected_email
            )

            admin_auth.delete_user(
                user_record.uid
            )

            st.success(
                "User deleted successfully"
            )

            st.rerun()

    # ===================================
    # SYSTEM TAB
    # ===================================

    with tab2:

        st.subheader(
            "📊 System Monitoring"
        )

        st.subheader(
    "🌐 API Status"
)

try:

    headers = {

        "x-api-key":
        st.secrets["API_KEY"]

    }

    response = requests.get(

        "https://apiforsmartplanter.onrender.com/history",

        headers=headers,

        timeout=5

    )

    if response.status_code == 200:

        st.success(
            "✅ API Online"
        )

    else:

        st.warning(
            f"⚠ API returned {response.status_code}"
        )

except:

    st.error(
        "❌ API Offline"
    )