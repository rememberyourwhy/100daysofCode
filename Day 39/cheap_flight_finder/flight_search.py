import requests
import json
from flight_data import FlightData


TEQUILA_API_KEY = "tl0o_1zNQ_K3hzIStU3HYPcI8XXnOf7y"
DEFAULT_URL = "https://tequila-api.kiwi.com"
SEARCH_QUERY_URL = f"{DEFAULT_URL}/locations/query"
SEARCH_BASIC_URL = f"{DEFAULT_URL}/v2/search"

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
            "location_types": "city"
        }
        response = requests.get(url=SEARCH_QUERY_URL, headers=headers, params=parameters)
        code = response.json()["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"

        }

        response = requests.get(url=SEARCH_BASIC_URL, headers=headers, params=parameters)

        # create flight data object that has attributes:
        # price
        # origin_city
        # origin_airport
        # destination_city
        # destination_airport
        # out_date
        # return_date
        #def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date,
        #return_date):

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")

        return response


# flight_search = FlightSearch()
# result_json = flight_search.get_destination_code("London").json()
# with open(file="search_result.json", mode="w") as search_result_file:
#     json.dump(result_json, search_result_file, indent=4)
# result = flight_search.get_destination_code("London")
# print(result)

# flight_search = FlightSearch()
# result = flight_search.check_flights(
#     origin_city_code="LON",
#     destination_city_code="BER",
#     from_time="31/08/2022",
#     to_time="31/12/2022"
# )
# result_json = result.json()
# with open(file="flight_search.json", mode="w") as flight_search_json:
#     json.dump(result_json, flight_search_json, indent=4)
# result = flight_search.get_destination_code("London")
# print(result)
