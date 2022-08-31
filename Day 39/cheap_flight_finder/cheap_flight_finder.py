# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
import json
from datetime import datetime, timedelta

ORIGIN_CITY_IATA = "LON"
MONTHS_LATER = 6

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

date_from = datetime.now() + timedelta(days=1)
date_to = datetime.now() + timedelta(days=30*MONTHS_LATER)

for destination in sheet_data:
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        date_from,
        date_to
    )



