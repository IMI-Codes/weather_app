from geopy.geocoders import Nominatim
import requests
import geocoder
from helpers import BASE_URL, API_KEY


g = geocoder.ip("me")
latitude, longitude = g.latlng
current_lat = latitude
current_long = longitude

second_half = f"lat={latitude}&lon={longitude}&appid={API_KEY}"
final_url = f"{BASE_URL}{second_half}"
data = requests.get(final_url)
print(data.json())

# clean up and refine


# Initialize the geolocator with a custom user-agent
geolocator = Nominatim(
    user_agent="my_geocoder_app"
)  # Replace "my_geocoder_app" with your app name

# Get the location details
location_name = "Kaduna"
location = geolocator.geocode(location_name)

# Check if the location was found and print details
if location:
    print(f"Location: {location_name}")
    print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")  # type: ignore
else:
    print(f"Could not find location: {location_name}")
