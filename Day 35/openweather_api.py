import requests
import json

LATITUDE = 16.066187
LONGITUDE = 108.212910
UNITS_OF_MEASUREMENT = "metric"

api_key = "8dc1a372b6d8c125d3f718a9b1457da9"
# Current: OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
# Forecast
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"

# Parameters:
# Parameters
# lat, lon	required	Geographical coordinates (latitude, longitude). If you need the geocoder to automatic convert city names and zip-codes to geo coordinates and the other way around, please use our Geocoding API.
# appid	required	Your unique API key (you can always find it on your account page under the "API key" tab)
# units	optional	Units of measurement. standard, metric and imperial units are available. If you do not use the units parameter, standard units will be applied by default. Learn more
# mode	optional	Response format. JSON format is used by default. To get data in XML format use mode=xml. Learn more
# cnt	optional	A number of timestamps, which will be returned in the API response. Learn more
# units	optional	Units of measurement. standard, metric and imperial units are available. If you do not use the units parameter, standard units will be applied by default. Learn more
# lang	optional	You can use the lang parameter to get the output in your language. Learn more

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_key,
    "units": UNITS_OF_MEASUREMENT
}

response = requests.get(url=OWM_Endpoint, params=parameters)
with open("OWM_data.json", mode="w") as json_data:
    new_data = response.json()
    json.dump(new_data, json_data, indent=4)
