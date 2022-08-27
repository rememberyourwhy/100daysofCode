import requests

from datetime import datetime


# --------------------------- CONSTANTS ----------------- #
LATITUDE = 16.066187
LONGITUDE = 108.212910

parameters = {
    "lat": LATITUDE,
    "long": LONGITUDE,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print([sunrise, sunset])  # 12 hours format

sunrise_time = sunrise.split("T")[1]
sunrise_hour = int(sunrise_time.split(":")[0])
sunset_time = sunset.split("T")[1]
sunset_hour = int(sunset_time.split(":")[0])

print(sunrise_hour)
print(sunset_hour)
now_hour = datetime.now().hour

if now_hour < sunrise_hour:
    print("The sun hasn't rise yet")
elif now_hour > sunset_hour:
    print("The sun is set")
else:
    print("The sun is still somewhere on the sky")