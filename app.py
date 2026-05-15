import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="MargDarshak AI",
    page_icon="🚀",
    layout="centered"
)

# ==========================================
# TITLE
# ==========================================

st.title("🚀 MargDarshak AI")

st.subheader("Hyperlocal Mobility Intelligence")

# ==========================================
# USER INPUTS
# ==========================================

start_location = st.text_input("Start Location")

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
# ANALYZE BUTTON
# ==========================================

if st.button("Analyze Mobility"):

    st.success("Analysis Running")

    # ==========================================
    # WEATHER SECTION
    # ==========================================

    st.write("## 🌤 Weather Analysis")

    weather_condition = "Haze"
    temperature = 32
    humidity = 70

    st.info(f"""
Weather Condition: {weather_condition}

Temperature: {temperature} °C

Humidity: {humidity}%
""")

    # ==========================================
    # MULTI ROUTE ENGINE
    # ==========================================

    st.write("## 🚗 Multi Route Analysis")

    routes = []

    # ==========================================
    # ROUTE 1
    # ==========================================

    route1_eta = 30
    route1_congestion = "Low"
    route1_score = 85

    if traffic == "High":
        route1_eta += 15
        route1_score -= 20

    if event == "Yes":
        route1_eta += 10
        route1_score -= 10

    # ==========================================
    # ROUTE 2
    # ==========================================

    route2_eta = 42
    route2_congestion = "Medium"
    route2_score = 70

    if traffic == "High":
        route2_eta += 20
        route2_score -= 15

    if event == "Yes":
        route2_eta += 8
        route2_score -= 5

    # ==========================================
    # ROUTE 3
    # ==========================================

    route3_eta = 55
    route3_congestion = "High"
    route3_score = 50

    if traffic == "High":
        route3_eta += 25
        route3_score -= 20

    if event == "Yes":
        route3_eta += 12
        route3_score -= 8

    # ==========================================
    # ADD ROUTES
    # ==========================================

    routes.append({
        "name": "Western Express Highway",
        "eta": route1_eta,
        "congestion": route1_congestion,
        "score": route1_score
    })

    routes.append({
        "name": "Eastern Freeway",
        "eta": route2_eta,
        "congestion": route2_congestion,
        "score": route2_score
    })

    routes.append({
        "name": "JVLR Connector",
        "eta": route3_eta,
        "congestion": route3_congestion,
        "score": route3_score
    })

    # ==========================================
    # DISPLAY ROUTES
    # ==========================================

    for route in routes:

        st.write("---")

        st.subheader(route["name"])

        st.write(f"⏱ ETA: {route['eta']} mins")

        st.write(f"🚦 Congestion: {route['congestion']}")

        st.write(f"🧠 Mobility Score: {route['score']}/100")

    # ==========================================
    # BEST ROUTE
    # ==========================================

    best_route = max(routes, key=lambda x: x["score"])

    st.write("---")

    st.write("## 🏆 AI Recommended Route")

    st.success(best_route["name"])

    st.write(f"""
Best ETA: {best_route['eta']} mins

Mobility Score: {best_route['score']}/100
""")

    # ==========================================
    # AI REASONING
    # ==========================================

    st.write("## 🧠 AI Reasoning")

    reasoning = []

    if best_route["congestion"] == "Low":
        reasoning.append("Lowest congestion detected")

    if best_route["eta"] < 40:
        reasoning.append("Fastest estimated travel time")

    if best_route["score"] > 80:
        reasoning.append("Highest mobility optimization score")

    if event == "Yes":
        reasoning.append("Adjusted for nearby public events")

    reasoning.append("Dynamic mobility optimization completed")

    for reason in reasoning:
        st.write(f"✅ {reason}")

    # ==========================================
    # FINAL INSIGHT
    # ==========================================

    st.write("---")

    st.write("## 📊 Final Mobility Insight")

    if traffic == "High":
        st.error("Heavy traffic detected across parts of the route network.")

    elif traffic == "Medium":
        st.warning("Moderate congestion detected.")

    else:
        st.success("Traffic conditions are favorable.")

    if event == "Yes":
        st.warning("Large public event may impact travel times.")

    else:
        st.info("No major mobility disruptions detected.")
