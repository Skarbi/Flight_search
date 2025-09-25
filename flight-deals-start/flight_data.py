from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()
class FlightData:
    def __init__(self):
        self.data_manager = DataManager()
        self.flight_search = FlightSearch()
        self.sheet_details = data_manager.info_from_the_sheet()


    def mulitple_city_flight_details(self,departure_date):
        access_token_response = flight_search.getting_access_token()
        for city in self.sheet_details['prices']:
            print(city)
            print(city["iataCode"], city['lowestPrice'])
            flight_search.flight_data_search(
                origin="KRK",
                destination=f"{city["iataCode"]}",
                departure_date=f"{departure_date}",
                adults=2,non_stop="false",
                currency_code="EUR",
                max_price=f"{city['lowestPrice']}",
                flight_numbers=1,
                access_token=access_token_response
            )



