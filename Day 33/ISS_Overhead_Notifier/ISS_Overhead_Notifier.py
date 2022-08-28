# Two things that we have to satisfy:
# Have a function that check time if it's night
# Have a function that check ISS position and our to see if the two position have +- 5 degrees diff

import requests

from datetime import datetime


# --------------------------- CONSTANTS ----------------- #
LATITUDE = 16.066187
LONGITUDE = 108.212910


def check_night_time():
    # ------------------------- GET REQUEST ------------------------ #
    parameters = {
        "lat": LATITUDE,
        "long": LONGITUDE,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()

    # ------------------------------- COMPARE TIME --------------------------------- #
    sunset = data["results"]["sunset"]

    sunset_time = sunset.split("T")[1]
    sunset_hour = int(sunset_time.split(":")[0])

    now_hour = datetime.now().hour

    if now_hour > sunset_hour:
        return True
    else:
        return False


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]

    iss_position = [longitude, latitude]
    my_position = [LONGITUDE, LATITUDE]

    diff_position = [abs(iss_position[x] - my_position[x]) for x in range(2)]
    if max(diff_position) <= 5:
        return True
    return False


if check_night_time() and is_iss_overhead():
    print(True)
else:
    print(False)
