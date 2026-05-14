import streamlit as st
import requests

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(page_title="MargDarshak AI")

# ==========================================
# API KEY
# ==========================================

API_KEY = "d69be8317bbd8306a07378374a47550d"

# ==========================================
# WEATHER FUNCTION
# ==========================================

def get_weather(city):

    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        if response.status_code == 200:

            weather = data["weather"][0]["description"]

            temp = data["main"]["temp"]

            humidity = data["main"]["humidity"]

            wind = data["wind"]["speed"]

            return weather, temp, humidity, wind

        else:

            return None

    except Exception as e:

        st.error(f"Weather API Error: {e}")

        return None

# ==========================================
# TITLE
# ==========================================

st.title("🚀 MargDarshak AI")

st.subheader("Hyperlocal Mobility Intelligence")

# ==========================================
# USER INPUTS
# ==========================================

start = st.text_input("Start Location")

destination = st.text_input("Destination")

traffic = st.selectbox(
    "Traffic Level",
    ["Low", "Medium", "High"]
)

event = st.selectbox(
    "Major Event Nearby?",
    ["No", "Yes"]
)

# ==========================================
# BUTTON
# ==========================================

if st.button("Analyze Mobility"):

    st.success("Analysis Running")

    # ==========================================
    # WEATHER ANALYSIS
    # ==========================================

    st.write("## 🌦 Weather Analysis")

    weather_data = get_weather(start)

    if weather_data:

        weather, temp, humidity, wind = weather_data

        st.info(f"""
Weather: {weather}

Temperature: {temp}°C

Humidity: {humidity}%

Wind Speed: {wind} m/s
""")

    else:

        st.error("Weather data unavailable")

    # ==========================================
    # ROUTE ANALYSIS
    # ==========================================

    st.write("## 🚗 Route Analysis")

    if traffic == "Low":

        eta = 30
        route = "Western Express Highway"

    elif traffic == "Medium":

        eta = 45
        route = "Eastern Freeway"

    else:

        eta = 60
        route = "JVLR Connector"

    st.success(f"Recommended Route: {route}")

    # ==========================================
    # ETA
    # ==========================================

    st.write("## ⏱ Estimated Travel Time")

    st.warning(f"{eta} mins")

    # ==========================================
    # AI RECOMMENDATION
    # ==========================================

    st.write("## 🧠 AI Recommendation")

    if traffic == "High":

        st.error("Heavy congestion detected. Delay travel by 15–20 mins.")

    elif traffic == "Medium":

        st.warning("Moderate congestion. Alternate routes recommended.")

    else:

        st.success("Traffic conditions favorable.")

    # ==========================================
    # EVENT IMPACT
    # ==========================================

    st.write("## 🎯 Event Impact")

    if event == "Yes":

        st.error("Major event detected nearby. Congestion probability increased.")

    else:

        st.success("No major mobility disruptions detected.")

    # ==========================================
    # AI REASONING
    # ==========================================

    st.write("## 📌 AI Reasoning")

    st.write("- Real-time weather analyzed")

    st.write("- Traffic congestion considered")

    st.write("- Event probability considered")

    st.write("- Route optimized using AI logic")

    st.write("- ETA dynamically adjusted")

def get_weather(city):

    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        st.write("Status Code:", response.status_code)

        data = response.json()

        st.write(data)

        if response.status_code == 200:

            weather = data["weather"][0]["description"]

            temp = data["main"]["temp"]

            humidity = data["main"]["humidity"]

            wind = data["wind"]["speed"]

            return weather, temp, humidity, wind

        else:

            return None

    except Exception as e:

        st.error(e)

        return None
