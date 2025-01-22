from weather_functions import *


# getting current location Data

current_lat_long = get_current_location_data()

url = url_builder(current_lat_long())  # type: ignore

data = get_weather_data(url)

print(data)
