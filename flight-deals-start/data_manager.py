import requests

SHEETY_URL = "https://api.sheety.co/1e3077f783705e3aa36e06a3413c4177/czymDlaCiebieJestCzasWolny/prices"

class DataManager:

    def info_from_the_sheet(self):

        response = requests.get(url=SHEETY_URL)
        #print(response.raise_for_status())
        return response.json()

