import requests

NUMBER_OF_QUESTIONS = 10
TYPE = "boolean"

parameters = {
    "amount": NUMBER_OF_QUESTIONS,
    "type": TYPE
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)

question_data = response.json()["results"]
