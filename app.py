import streamlit as st

st.set_page_config(page_title="MargDarshak AI")

st.title("🚀 MargDarshak AI")

st.subheader("Hyperlocal Mobility Intelligence")

# =========================
# INPUTS
# =========================

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

# =========================
# ANALYZE BUTTON
# =========================

if st.button("Analyze Mobility"):

    st.success("Analysis Running")

    st.write("## 🌦 Weather")
    st.info("Haze | 31°C")

    st.write("## 🚗 Recommended Route")
    st.success("Western Express Highway")

    st.write("## ⏱ ETA")
    st.warning("42 mins")

    st.write("## 🧠 AI Recommendation")

    if traffic == "High":
        st.error("Wait 15 mins before departure")
    else:
        st.success("Good time to leave")

    st.write("## 📌 Reasoning")

    st.write("- Moderate congestion detected")
    st.write("- Weather stable")
    st.write("- Mobility score optimized")
    st.info("Haze | 31°C")
    import requests
    API_KEY = "YOUR_OPENWEATHER_API_KEY"

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data.get("main"):

        weather = data["weather"][0]["description"]

        temp = data["main"]["temp"]

        humidity = data["main"]["humidity"]

        return weather, temp, humidity

    return None
    weather_data = get_weather(start)

if weather_data:

    weather, temp, humidity = weather_data

    st.info(f"{weather} | {temp}°C | Humidity: {humidity}%")

else:

    st.error("Weather data unavailable")
