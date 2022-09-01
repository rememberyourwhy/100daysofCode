import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/e1c79acdae9fa0ea0870ae8ac40fdc28/flightDeals/users"

# First Name # Last Name # Email

# response = requests.get(url=SHEETY_PRICES_ENDPOINT)
# data = response.json()
# sheet_data = data["users"]
#
# non_data_id = sheet_data[-1]["id"] + 1
# This id value is necessary if we use requests.put method, but since we are going to use requests.post, it'll be fine

user_first_name = input("What is your first name? ")
user_last_name = input("What is your last name? ")
user_email = input("What is your email? ")

new_data = {
    "user": {
        "firstName": user_first_name,
        "lastName": user_last_name,
        "email": user_email
    }
}

# put_url = f"{SHEETY_PRICES_ENDPOINT}/{non_data_id}"
post_url = SHEETY_PRICES_ENDPOINT
response = requests.post(
    url=post_url,
    json=new_data
)

if response.status_code == 200:
    print("User is successfully added")

