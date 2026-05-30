import streamlit as st

def AboutPage():

    st.title("About")

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