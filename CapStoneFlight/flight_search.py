import requests

from data_manager import DataManager
from flight_data import FlightData
KIWIAPI = "OJT_GTPNwiDa9X5j4EoSFPTP-xsk_SRK"
FLYEND = "https://api.tequila.kiwi.com/v2/search"

HEADERS = {
    "apikey":KIWIAPI
}

class FlightSearch:


   def check_flights(self,origin_city_code,destination_city_code,from_time,to_time):
       query = {
           "fly_from":origin_city_code,
           "fly_to":destination_city_code,
           "date_from":from_time.strftime("%d/%m/%Y"),
           "date_to":to_time.strftime("%d/%m/%Y"),
           "nights_in_dst_from":7,
           "nights_in_dst_to":28,
           "flight_type":"round",
           "one_for_city":1,
           "max_stopovers":0,
           "curr":"GBP"
       }


       response = requests.get(url=FLYEND,headers=HEADERS,params=query)
       data = response.json()["data"][0]

       flight_data = FlightData(
           price=data["price"],
           origin_city=data["route"][0]["cityFrom"],
           origin_airport=data["route"][0]["flyFrom"],
           destination_city=data["route"][0]["cityTo"],
           destination_airport=data["route"][0]["flyTo"],
           out_date=data["route"][0]["local_departure"].split("T")[0],
           return_date=data["route"][1]["local_departure"].split("T")[0]
       )
       print(f"{flight_data.destination_city}: £{flight_data.price}")
       return flight_data
