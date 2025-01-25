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


# this works


def url_builder(values: dict):
    co_ordinates = values
    latitude = values["latitude"]
    longitude = values["longitude"]
    second_half = f"lat={latitude}&lon={longitude}&appid={API_KEY}"
    final_url = f"{BASE_URL}{second_half}"
    return final_url


# this works


def get_weather_data(url):
    data = requests.get(url)
    return data.json()


# this works
