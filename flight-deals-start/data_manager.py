import requests
from dotenv import load_dotenv
import os

load_dotenv()
SHEETY_URL = os.getenv("SHEETY_URL")
class DataManager:

    def info_from_the_sheet(self):

        response = requests.get(url=SHEETY_URL)
        #print(response.raise_for_status())
        return response.json()

