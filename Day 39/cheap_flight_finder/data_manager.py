import requests
import json

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/e1c79acdae9fa0ea0870ae8ac40fdc28/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    # Bad version:
    # def get_destination_data(self):
    #     sheety_get_data = requests.get(url=SHEETY_PRICES_ENDPOINT).json()
    #     # Make a json output to get better data visualizing
    #     # with open("sheety_get_data.json", mode="w") as sheety_response_json:
    #     #     json.dump(sheety_get_data, sheety_response_json, indent=4)
    #     self.destination_data = sheety_get_data["prices"]
    #     return self.destination_data

    # Better comprehension version:
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            url = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
            response = requests.put(
                url=url,
                json=new_data
            )
            print(response.text)


# MANUALLY CHANGING IATA CODE COLUMN VALUES TO TEST IF THE UPDATE FUNCTION WORKS GOOD

# data_manager = DataManager()
# data = data_manager.get_destination_data()
# for city in data_manager.destination_data:
#     city["iataCode"] = "TESTING"
# data_manager.update_destination_codes()
# response = requests.get(url=SHEETY_PRICES_ENDPOINT)
# with open(file="after_adding_iata_code.json", mode="w") as result_json_file:
#     result_data = response.json()
#     json.dump(result_data, result_json_file, indent=4)
