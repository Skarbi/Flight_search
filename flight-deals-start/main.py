#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time

from data_manager import DataManager
from flight_data import FlightData
# from flight_search import
# from notification_manager import
from datetime import  datetime, timedelta
from time import strftime
data_manager = DataManager()
flight_data = FlightData()

period = []
today = datetime.now().strftime("%Y-%m-%d")

#Check for the flight for another 90 days
for number_days in range(90):
    new_date = datetime.strptime(today, "%Y-%m-%d") + timedelta(days=number_days)

    flight_data.mulitple_city_flight_details(departure_date=new_date.strftime("%Y-%m-%d"))



