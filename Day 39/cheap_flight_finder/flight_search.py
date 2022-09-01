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

    @staticmethod
    def get_destination_code(city_name):
        parameters = {
            "term": city_name,
            "limit": IATA_CODE_RESULT_LIMIT,
            "location_types": "city"
        }
        response = requests.get(url=SEARCH_QUERY_URL, headers=headers, params=parameters)
        code = response.json()["locations"][0]["code"]
        return code

    @staticmethod
    def check_flights(origin_city_code, destination_city_code, from_time, to_time):
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            # "one_for_city": 1,
            # "max_stopovers": 100,
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
        # def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date,
        # return_date):

        try:
            # data = response.json()["data"][0]

            data = response.json()["data"][-1]

        except IndexError:
            print(f"No 0 stop flights found for {destination_city_code}.")
            parameters["max_stopovers"] = 1
            response = requests.get(url=SEARCH_BASIC_URL, headers=headers, params=parameters)
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No 1 stop flights found for {destination_city_code}.")
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
        if destination_city_code == "TYO":
            for random_data in response.json()["data"]:
                if len(random_data["route"]) == 8:
                    data = random_data
                    break
            for flight in data["route"]:
                if flight["cityCodeTo"] == destination_city_code:
                    flight_contain_destination = flight
                    break

            flight_data.destination_city = flight_contain_destination["cityTo"],
            flight_data.destination_airport = flight_contain_destination["flyTo"],
            flight_data.return_date = flight_contain_destination["local_departure"].split("T")[0]
            flight_data.stop_overs = len(data["route"]) - 2
            # get via_city values from "city_from" from ["route"][1] to ["route'][len["route"] - 2]
            via_cities_list = [stop_over["cityFrom"] for stop_over in data["route"][1:] if stop_over["cityCodeFrom"] != destination_city_code]
            flight_data.via_city = "||".join(via_cities_list)
            print(f"number of stop overs: {flight_data.stop_overs}")
            print(f"via cities: {flight_data.via_city}")
        print(f"{flight_data.destination_city}: £{flight_data.price}")

        return flight_data

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
