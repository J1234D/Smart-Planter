import streamlit as st


def ProfilePage(db,user):

    st.title("👤 User Profile")

    st.subheader(
        "Profile Settings"
    )

    uid = user["localId"]

    profile = (

        db.collection("users")

        .document(uid)

        .get()

    )

    profile_data = profile.to_dict()

    st.subheader(
    "📄 Account Information"
    )

    st.write(
        f"📧 Email: {profile_data['email']}"
    )

    st.write(
        f"🎨 Theme: {profile_data['theme']}"
    )

    st.write(
        f"🔔 Notifications: {profile_data['notifications']}"
    )