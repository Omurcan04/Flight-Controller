import requests

SHEETY = "https://api.sheety.co/df8360f7a841656591661f8d2ff4d48f/flightdeals/prices"
class DataManager:

    def __init__(self):
        self.destination_data ={}



    def get_destination_data(self):
        response = requests.get(url=SHEETY)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data



