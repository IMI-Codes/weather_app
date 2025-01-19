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

# for entered location convert location to long and lat
