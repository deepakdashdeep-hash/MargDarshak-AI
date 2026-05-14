# ===== GLOBAL CITY WEATHER ENGINE =====

import requests

# =========================
# OPENWEATHER API KEY
# =========================

API_KEY = "07d3598a007f603f4b6c10c31ee9166e"

# =========================
# USER INPUT
# =========================

city = input("Enter City Name Anywhere in the World: ")

# =========================
# WEATHER API URL
# =========================

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# =========================
# FETCH DATA
# =========================

response = requests.get(url)

data = response.json()

# =========================
# CHECK RESPONSE
# =========================

if data["cod"] == 200:

    # =========================
    # EXTRACT WEATHER DATA
    # =========================

    city_name = data["name"]

    country = data["sys"]["country"]

    weather = data["weather"][0]["description"]

    temperature = data["main"]["temp"]

    feels_like = data["main"]["feels_like"]

    humidity = data["main"]["humidity"]

    wind_speed = data["wind"]["speed"]

    pressure = data["main"]["pressure"]

    visibility = data.get("visibility", 0) / 1000

    # =========================
    # DISPLAY REPORT
    # =========================

    print("\n===== GLOBAL WEATHER INTELLIGENCE =====")

    print(f"\nCity: {city_name}")

    print(f"Country: {country}")

    print(f"Weather: {weather}")

    print(f"Temperature: {temperature}°C")

    print(f"Feels Like: {feels_like}°C")

    print(f"Humidity: {humidity}%")

    print(f"Wind Speed: {wind_speed} m/s")

    print(f"Pressure: {pressure} hPa")

    print(f"Visibility: {visibility} km")

    # =========================
    # AI WEATHER ANALYSIS
    # =========================

    print("\n===== AI WEATHER ANALYSIS =====")

    if "rain" in weather.lower():

        print("\n⚠ Rain detected.")

        print("Possible traffic slowdown.")

        print("Road braking distance may increase.")

    elif "storm" in weather.lower():

        print("\n⚠ Storm conditions detected.")

        print("High mobility disruption expected.")

    elif "snow" in weather.lower():

        print("\n⚠ Snow conditions detected.")

        print("Slippery roads and delays likely.")

    elif "clear" in weather.lower():

        print("\n✅ Clear weather conditions.")

        print("Good mobility efficiency expected.")

    elif "haze" in weather.lower() or "fog" in weather.lower():

        print("\n⚠ Reduced visibility conditions.")

        print("Possible slower traffic movement.")

    else:

        print("\nℹ Moderate weather conditions.")

# =========================
# ERROR HANDLING
# =========================

else:

    print("\n❌ City not found or weather unavailable.")

    print("Try entering a larger or more recognized city.")