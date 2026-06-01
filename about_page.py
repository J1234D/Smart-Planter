import streamlit as st

def AboutPage():
    st.image("https://ststephensbirati.in/wp-content/uploads/2021/07/12X-12LOGO_New_2023-768x956.png",width=70)
    
    st.title("About Smart Planter")

    col1,col2 = st.columns(2)

    with col1:

        st.write("""

Smart Planter is an IoT-based plant monitoring system designed to help users track the health of their plants in real time.

The system collects environmental data from sensors connected to an ESP32 microcontroller, including:

Soil Moisture
Soil pH
Day/Night Status
Timestamped Readings

Sensor data is sent securely to a cloud-based API, where it is processed and stored for analysis. The dashboard provides live monitoring, historical trends, and insights to help users understand their plant's growing conditions.

### Features

✅ Real-Time Sensor Monitoring

✅ Historical Data Tracking

✅ Cloud-Based Data Storage

✅ Interactive Dashboard

✅ Plant Health Insights

Technology Stack
             
- ESP32 Microcontroller
- FastAPI Backend
- Streamlit Dashboard
- Google Sheets Data Storage
- Python
- Project Goal

The goal of Smart Planter is to make plant care more accessible by combining sensors, cloud technology, and data visualization into a simple and user-friendly platform.

This project demonstrates the integration of IoT hardware, web development, APIs, cloud storage, and data analytics in a practical real-world application.

Built with Python, IoT, and a passion for learning.


""")
        with col1:
            st.image("flowchart.png",width=2500)

    st.markdown("""<h2>Designed by Students of </h2>
    <h1 style='text-align: center; color: white;'>
        St. Stephen's School, Birati
    </h1>
    <h3 style='text-align: center; color: white;'>
        KOLKATA, WEST BENGAL, INDIA
    </h3>
    """,
    unsafe_allow_html=True
)