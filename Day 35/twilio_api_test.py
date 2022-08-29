import requests
import json
from datetime import datetime
from twilio.rest import Client


# ----------------------------------- CONSTANTS --------------------- #
LATITUDE = 16.066187
LONGITUDE = 108.212910
UNITS_OF_MEASUREMENT = "metric"
FORECAST_TIME = 24
account_sid = "AC221225c316e96bd94add07ab8bdc06e6"
auth_token = "81b826bdf5d74272510c38b814781c0f"


api_key = "8dc1a372b6d8c125d3f718a9b1457da9"
# Current: OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
# Forecast
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"

# ---------------------------------- OWM API ------------------------ #
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

weather_data = response.json()["list"]

# ---------------------- GET TIME NOW -------------------- #
# use datetime module to get datetime when the program run and change it to fit 3 hours gap in the data

time_now = datetime.now().hour + 1
time_now_formatted = time_now - (time_now % 3)

# --------------- WILL RAIN IN 12 HOURS ? ---------- #
# find the first 3 hours forecast that near current time
# strip "dt_txt" value from dictionary to get the "hour" value (time)
# get the first time that fit current time


def will_rain():
    index = 0
    while index < len(weather_data):
        forecast_daytime = weather_data[index]["dt_txt"]    # 2022-08-29 21:00:00
        forecast_time = forecast_daytime.split(" ")[1]      # 21:00:00
        forecast_hour = forecast_time.split(":")[0]         # 21
        forecast_hour = int(forecast_hour)
        if forecast_hour == time_now_formatted:
            break
        index += 1

    number_of_forecast_to_check = FORECAST_TIME // 3 + 1

    for _ in range(index, index + number_of_forecast_to_check):    # 12 HOUR = 4 PORTIONS OF 3 HOURS = 5 FORECASTS WITH 3 HOUR GAP
        fore_cast_dict = weather_data[_]
        if fore_cast_dict["weather"][0]["main"] == "Rain":
            return True
    return False


# -------------------------- twilio API --------------------- #
def send_message():
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="It's going to rain today. Bring raincoat",
                         from_='+16187875863',
                         to='+84379809157'
                     )
    print(message.status)


if will_rain():
    send_message()