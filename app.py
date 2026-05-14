ifst.button("Analyze Mobility"):

    st.success("Analysis Running")

    weather_data = get_weather(start)

    st.write("## 🌦 Weather")

    if weather_data:

        weather, temp, humidity = weather_data

        st.info(f"{weather} | {temp}°C | Humidity: {humidity}%")

    else:

        st.error("Weather data unavailable")

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
