import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "rememberyourwhyPt17122003"
USERNAME = "tp"
GRAPH_ID = "graph01"

# parameters:
# Key	Type	Description
# token	string	[required] A token string used to authenticate as a user to be created.
#   The token string is hashed and saved.
# Validation rule: [ -~]{8,128}
# username	string	[required] User name for this service.
# Validation rule: [a-z][a-z0-9-]{1,32}
# agreeTermsOfService	string	[required] Specify yes or no whether you agree to the terms of service.
# Please see: Terms of service - Japanese version / Terms of service - English version
# notMinor	string	[required] Specify yes or no whether you are not a minor or if you are a minor,
#   and you have the parental consent of using this service.
# thanksCode	string	[optional] Set thanks-code .
#   If it is a valid thanks-code, some limited features will be available.
#   For details, please check How to support Pixela by Patreon ／ Use Limited Features.

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# 1. Create your user account

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# 2.Create a graph account

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "English Reading Graph",
    "unit": "page",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")
# today = datetime(year=2022, month=8, day=30)

# 2.Create a pixel

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": today_formatted,
    "quantity": input("How many pages did you read today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"

pixel_update_data = {
    "quantity": "100"
}

# requests.put(url=pixel_update_endpoint, json=pixel_data, headers=headers)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response)
