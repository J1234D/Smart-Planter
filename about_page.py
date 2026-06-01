import streamlit as st


def AboutPage():

    st.image(
        "https://ststephensbirati.in/wp-content/uploads/2021/07/12X-12LOGO_New_2023-768x956.png",
        width=70
    )

    st.title("🌱 About Smart Planter")

    st.write("""

Smart Planter is an IoT-based plant monitoring and analytics system designed to help users monitor plant health in real time using sensors, cloud computing, and interactive data visualization.

The system uses multiple ESP32 microcontrollers connected to environmental sensors to continuously collect important plant health data such as:

• Soil Moisture  
• Soil pH  
• Day/Night Status  
• Timestamped Sensor Readings  

The sensor data is securely transmitted to a FastAPI cloud backend, where it is processed, analyzed, and stored in Firebase Firestore for historical tracking and analytics.

The Streamlit dashboard provides a modern interface for:

✅ Real-Time Plant Monitoring  
✅ Multi-Plant Management  
✅ Historical Data Visualization  
✅ Plant Health Alerts  
✅ Cloud-Based Data Storage  
✅ Interactive Analytics Charts  
✅ Mobile Notifications using ntfy  

━━━━━━━━━━━━━━━━━━━━━━

## 🧠 System Architecture

The Smart Planter architecture consists of:

ESP32 Devices  
↓  
FastAPI Backend (Render Cloud)  
↓  
Firebase Firestore Database  
↓  
Streamlit Dashboard & Analytics  
↓  
Mobile Notification System  

The project supports multiple plants simultaneously using unique plant IDs and plant-specific monitoring rules.

Each plant maintains:

• Independent live data  
• Separate historical records  
• Individual alerts and analytics  
• Plant-specific health rules  

━━━━━━━━━━━━━━━━━━━━━━

## 📊 Analytics Features

The analytics system allows users to:

• View Moisture Trends  
• View pH Trends  
• Filter Historical Data  
• Analyze Average Readings  
• Monitor Long-Term Plant Health  

Time-based filtering includes:

• Last 24 Hours  
• Last 7 Days  
• Last 30 Days  

━━━━━━━━━━━━━━━━━━━━━━

## 🔔 Smart Alert System

The backend continuously checks sensor data against plant-specific rules.

If abnormal conditions are detected, the system automatically sends mobile alerts such as:

⚠ Plant Needs Water  
🧪 Soil Too Acidic  
🧪 Soil Too Alkaline  

Notifications include:

• Plant ID  
• Plant Type  
• Alert Message  
• Timestamp  

━━━━━━━━━━━━━━━━━━━━━━

## 🛠 Technology Stack

• ESP32 Microcontroller  
• FastAPI Backend  
• Firebase Firestore  
• Streamlit Dashboard  
• Python  
• ntfy Notification System  
• IoT Sensor Integration  

━━━━━━━━━━━━━━━━━━━━━━

## 🎯 Project Goal

The goal of Smart Planter is to make plant care smarter, more accessible, and data-driven by combining IoT hardware, cloud technologies, APIs, analytics, and real-time monitoring into a unified platform.

This project demonstrates practical integration of:

• IoT Systems  
• Backend Development  
• Cloud Databases  
• Real-Time APIs  
• Data Analytics  
• Dashboard Development  
• Multi-Device Architecture  

━━━━━━━━━━━━━━━━━━━━━━

Built with Python, IoT, cloud technologies, and a passion for learning.

""")

    st.subheader(
        "System Architecture"
    )

    st.image(
        "flowchart.png",
        use_container_width=True
    )

    st.markdown(
        """
<h2 style='text-align: center;'>
Designed by Students of
</h2>

<h1 style='text-align: center; color: white;'>
St. Stephen's School, Birati
</h1>

<h3 style='text-align: center; color: white;'>
KOLKATA, WEST BENGAL, INDIA
</h3>
""",
        unsafe_allow_html=True
    )

