import requests
import json

AMADEUS_API_KEY = "4mXIv6Uz4GHSK4M7Z7gaqBP23KJTP3JL"
AMADEUS_API_SECRET = "aK4GP46rNVsSKTyA"
#______________________ GAINING ACCESS TOKEN
AMADEUS_TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
#______________________
AMADESU_SEARCH_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers?"
ACCESS_TOKEN = "0U9Iw2peYTjZ1ppfh4Wbhth0QqZG"

header = {
    "Authorization" : f"Bearer {ACCESS_TOKEN}"
}



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.search_criteria = "" # Do dopracowania
        self.header = {}
        self.body = {
            "grant_type": "client_credentials",
            "client_id": f"{AMADEUS_API_KEY}",
            "client_secret": f"{AMADEUS_API_SECRET}",
                }


    def flight_data_search(self,origin, destination,departure_date,adults,non_stop,currency_code,max_price,flight_numbers, access_token):
        self.search_criteria = (f"originLocationCode={origin}&"
                                f"destinationLocationCode={destination}&"
                                f"departureDate={departure_date}&"
                                f"adults={adults}&"
                                f"nonStop={non_stop}&"
                                f"currencyCode={currency_code}&"
                                f"maxPrice={max_price}&"
                                f"max={flight_numbers}")

        self.header = {
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.get(url=f"{AMADESU_SEARCH_URL}{self.search_criteria}", headers=self.header)
        print(json.dumps(response.json(), indent=2))
        return response.json()

    def getting_access_token(self):

        response = requests.post(url=f"{AMADEUS_TOKEN_URL}",
                                 headers={"Content-Type": "application/x-www-form-urlencoded"}, data=self.body)
        response_json = response.json()
        return response_json["access_token"]


