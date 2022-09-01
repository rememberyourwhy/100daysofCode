from twilio.rest import Client
from flight_data import FlightData

account_sid = "AC221225c316e96bd94add07ab8bdc06e6"
auth_token = "81b826bdf5d74272510c38b814781c0f"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self, flight_info):
        self.flight = flight_info
        print(type(flight_info))

    def send_notification(self):
        client = Client(account_sid, auth_token)

        body = f"Low price alert! Only £{self.flight.price} to " \
               f"fly from {self.flight.origin_city}_{self.flight.origin_airport} " \
               f"to {self.flight.destination_city}_{self.flight.destination_airport}, " \
               f"from {self.flight.out_date} to {self.flight.return_date}"
        # message = client.messages.create(
        #     body=body,
        #     from_='+16187875863',
        #     to='+84379809157'
        # )
        print(body)
