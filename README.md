# 🌱 Smart Planter

A full-stack IoT smart plant monitoring platform built with ESP32, FastAPI, Streamlit, Firebase Authentication, and Firestore.

## 🚀 Features

### 🌿 Plant Monitoring

* Live moisture monitoring
* Soil pH tracking
* Day/Night detection
* Plant health analysis
* Historical analytics and trends

### 🔐 Authentication System

* Firebase email/password authentication
* User accounts and sessions
* Admin-only protected routes
* Secure role-based access

### 🛡 Admin Panel

* View all registered users
* Disable/enable user accounts
* Delete accounts safely
* API health monitoring
* Protected admin account system

### 📊 Analytics Dashboard

* 24-hour, 7-day, and 30-day charts
* Historical sensor data
* Plant-specific filtering
* Real-time dashboard updates

### 👤 User Profiles

* Persistent Firestore user profiles
* User preferences system
* Notification settings
* Personalized user data

---

# 🏗 Tech Stack

## Hardware

* ESP32
* Soil moisture sensor
* pH sensor
* Light/day detection

## Backend

* FastAPI
* Firebase Admin SDK
* Firestore Database

## Frontend

* Streamlit
* Streamlit Option Menu
* Pandas
* Plotly/Charts

## Authentication

* Firebase Authentication
* Firestore user profiles

---

# ⚙ Architecture

ESP32 Sensors
↓
FastAPI Backend
↓
Firestore Database
↓
Streamlit Dashboard
↓
Firebase Authentication + Admin System

---

# 🔥 What I Learned While Building This

* Full-stack application architecture
* Firebase Authentication
* Firestore database design
* Role-based admin systems
* Backend API development
* IoT monitoring workflows
* User profile systems
* Cloud deployment
* Secure secrets management
* Real-time dashboards

---

# 📦 Installation

## Clone the repository

```bash
git clone https://github.com/J1234D/Smart-Planter
cd smart-planter
```

## Install dependencies

```bash
uv sync
```

## Run the Streamlit app

```bash
streamlit run app.py
```

## Run the FastAPI backend

```bash
uvicorn main:app --reload
```

---

# 🔑 Environment Variables

Create a `.streamlit/secrets.toml` file for:

* Firebase Admin credentials
* API keys
* Secret configuration

---

# 📈 Future Plans

* AI plant assistant
* Discord integration
* Plant disease detection
* Push notifications
* Profile pictures
* Multi-device management
* Battery + solar analytics
* Mobile-friendly UI

---

# 🧠 Why I Built This

I wanted to learn how real IoT platforms work by building a complete system myself — from ESP32 sensor collection all the way to authentication, analytics, admin dashboards, and cloud deployment.

This project helped me understand how hardware, APIs, databases, and frontend systems connect together in real-world applications.

---

# 📜 License

MIT License
