import requests
import json

TEQUILA_API_KEY = "tl0o_1zNQ_K3hzIStU3HYPcI8XXnOf7y"
REQUEST_URL = "https://tequila-api.kiwi.com/locations/query"

headers = {
    "apikey": TEQUILA_API_KEY,
    "Content-Type": "application/json"
}

IATA_CODE_RESULT_LIMIT = 1


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        parameters = {
            "term": city_name,
            "limit": IATA_CODE_RESULT_LIMIT,
            "location_types": "airport"
        }
        response = requests.get(url=REQUEST_URL, headers=headers, params=parameters)
        code = response.json()["locations"][0]["code"]
        return code


flight_search = FlightSearch()
# result_json = flight_search.get_destination_code("London").json()
# with open(file="search_result.json", mode="w") as search_result_file:
#     json.dump(result_json, search_result_file, indent=4)
result = flight_search.get_destination_code("London")
print(result)
