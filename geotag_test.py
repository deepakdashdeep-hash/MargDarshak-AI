from geopy.geocoders import Nominatim

# Initialize geocoder
geolocator = Nominatim(user_agent="MargDarshak")

# User input
location_name = input("Enter location: ")

# Fetch location
location = geolocator.geocode(location_name)

# Display results
if location:

    print("\n===== LOCATION DATA =====")

    print(f"\nAddress: {location.address}")

    print(f"Latitude: {location.latitude}")

    print(f"Longitude: {location.longitude}")

else:

    print("\n❌ Location not found.")