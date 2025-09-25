import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")

AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")
#______________________ GAINING ACCESS TOKEN
AMADEUS_TOKEN_URL = os.getenv("AMADEUS_TOKEN_URL")
#______________________
AMADESU_SEARCH_URL = os.getenv("AMADESU_SEARCH_URL")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

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
        #print(json.dumps(response.json(), indent=2))
        return response.json()

    def getting_access_token(self):

        response = requests.post(url=f"{AMADEUS_TOKEN_URL}",
                                 headers={"Content-Type": "application/x-www-form-urlencoded"}, data=self.body)
        response_json = response.json()
        return response_json["access_token"]


