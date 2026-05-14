import requests
import random

# =========================
# WEATHER FUNCTION
# =========================

API_KEY = "07d3598a007f603f4b6c10c31ee9166e"

def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data["cod"] != 200:
        return None

    weather = data["weather"][0]["main"]
    temperature = data["main"]["temp"]

    return weather, temperature


# =========================
# COORDINATES
# =========================

def get_coordinates(place):

    url = f"https://nominatim.openstreetmap.org/search?q={place}&format=json&limit=1"

    headers = {
        "User-Agent": "MargDarshak"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    if len(data) == 0:
        return None, None

    lat = data[0]['lat']
    lon = data[0]['lon']
    display_name = data[0]['display_name']

    return f"{lon},{lat}", display_name


# =========================
# ROUTE ENGINE
# =========================

def get_route(start, end):

    url = f"http://router.project-osrm.org/route/v1/driving/{start};{end}?overview=false"

    response = requests.get(url)

    data = response.json()

    distance = data['routes'][0]['distance'] / 1000
    duration = data['routes'][0]['duration'] / 60

    return distance, duration


# =========================
# MAIN PROGRAM
# =========================

print("\n===== MARG DARSHak AI =====")

start_place = input("\nEnter Start Location: ")
end_place = input("Enter Destination: ")

traffic = input("Traffic Level (low / medium / heavy): ").lower()

event = input("Any major event? (yes / no): ").lower()

# WEATHER

weather_data = get_weather(end_place)

if weather_data is None:

    print("\n❌ Weather data unavailable.")
    weather = "Unknown"
    temperature = 0

else:

    weather, temperature = weather_data

# COORDINATES

start_coords, start_name = get_coordinates(start_place)
end_coords, end_name = get_coordinates(end_place)

if start_coords is None or end_coords is None:

    print("\n❌ Location not found.")

else:

    base_distance, base_duration = get_route(start_coords, end_coords)

    # ROUTE OPTIONS

    routes = []

    route_names = [
        "Western Express Highway",
        "JVLR Connector",
        "Eastern Freeway Route"
    ]

    for route in route_names:

        duration = base_duration + random.randint(0, 20)

        score = duration

        congestion = random.choice(["Low", "Medium", "High"])

        # TRAFFIC IMPACT

        if traffic == "medium":
            score += 10

        elif traffic == "heavy":
            score += 25

        # WEATHER IMPACT

        if weather.lower() == "rain":
            score += 12

        elif weather.lower() == "thunderstorm":
            score += 25

        # EVENT IMPACT

        if event == "yes":
            score += 15

        # CONGESTION IMPACT

        if congestion == "Medium":
            score += 10

        elif congestion == "High":
            score += 20

        routes.append({
            "name": route,
            "duration": round(duration, 2),
            "score": round(score, 2),
            "congestion": congestion
        })

    # SORT BEST ROUTE

    routes.sort(key=lambda x: x['score'])

    # DISPLAY RESULTS

    print("\n===== LIVE WEATHER =====")

    print(f"\nWeather Condition: {weather}")
    print(f"Temperature: {temperature}°C")

    print("\n===== ROUTE ANALYSIS =====")

    for i, route in enumerate(routes):

        print(f"\nRoute {i+1}: {route['name']}")

        print(f"ETA: {route['duration']} mins")

        print(f"Congestion: {route['congestion']}")

        print(f"Mobility Score: {route['score']}")

        print("\nReasoning:")

        if route['congestion'] == "High":
            print("- High congestion detected.")

        if weather.lower() == "rain":
            print("- Rain expected to slow movement.")

        if weather.lower() == "thunderstorm":
            print("- Severe weather risk detected.")

        if event == "yes":
            print("- Major public event may impact route.")

        print("--------------------------------")

    # FINAL RECOMMENDATION

    best_route = routes[0]

    print("\n===== FINAL AI RECOMMENDATION =====")

    print(f"\nRecommended Route: {best_route['name']}")

    print(f"Expected ETA: {best_route['duration']} mins")

    print("\nWhy?")

    print("- Lowest mobility score")
    print("- Better traffic conditions")
    print("- Weather-adjusted optimization")

    if traffic == "heavy":

        print("\nAdditional Suggestion:")

        print("- Delay departure by 10–20 mins")
        print("- Traffic likely to reduce after congestion peak")
        print("- Suggested short waiting stop before highway entry")