import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
NUTRITIONIX_API_ID = os.getenv("NUTRITIONIX_API_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
SHEETY_API_ENDPOINT = os.getenv("SHEETY_API_ENDPOINT")
SHEETY_AUTHORIZATION = os.getenv("SHEETY_AUTHORIZATION")


natural_exercise_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me what exercises you did: ")

parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": 53.5,
    "height_cm": 173.64,
    "age": 21
}

natural_headers = {
    "x-app-id": NUTRITIONIX_API_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json"
}

natural_response = requests.post(
    url=natural_exercise_endpoint,
    json=parameters,
    headers=natural_headers
)
print(natural_response.text)
# with open("natural_language_exercise.json", mode="w") as natural_lang_exercise_json:
#     data = response.json()
#     json.dump(data, natural_lang_exercise_json, indent=4)



exercise_data = natural_response.json()["exercises"]

for exercise in exercise_data:
    now = datetime.now()
    exercise_date = now.strftime("%d/%m/%Y")
    exercise_time = now.strftime("%H:%M:%S")

    exercise_name = exercise["name"]
    exercise_duration = exercise["duration_min"]
    exercise_calories = exercise["nf_calories"]

    sheety_row_data = {
        "workout": {
            "date": exercise_date,
            "time": exercise_time,
            "exercise": exercise_name.title(),
            "duration": exercise_duration,
            "calories": exercise_calories
        }
    }

    sheety_headers = {
        "Content-Type": "application/json",
        "Authorization": SHEETY_AUTHORIZATION,
    }
    sheety_response = requests.post(
        url=SHEETY_API_ENDPOINT,
        json=sheety_row_data,
        headers=sheety_headers
    )
    print(sheety_response.text)
