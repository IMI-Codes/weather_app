from geopy.geocoders import Nominatim
import requests
import geocoder

API_KEY = "af99065f1b520a2248438ffc4deca409"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


def get_current_location_data():
    try:

        g = geocoder.ip("me")
        latitude, longitude = g.latlng
        return {"latitude": latitude, "longitude": longitude}
    except:
        print("Error Occurred")


def get_location_data(location: str):
    geolocator = Nominatim(user_agent="my_weather_app")
    location_name = location
    location_data = geolocator.geocode(location)
    if location:
        return {
            "latitude": location_data.latitude,  # type: ignore
            "longitude": location_data.longitude,  # type: ignore
        }
    else:
        print(f"Could not find location: {location}")


def url_builder(values: dict):
    latitude, longitude = values
    second_half = f"lat={latitude}&lon={longitude}&appid={API_KEY}"
    final_url = f"{BASE_URL}{second_half}"
    return final_url


def get_weather_data(url):
    data = requests.get(url)
    return data.json()
