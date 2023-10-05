import requests

SHEET_API = ' https://api.sheety.co/f0d56a52a8ad286c1af455d81e1e9359/flightDeals/prices'


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.city_code = {}
        self.city_lowest_price = {}
        self.city_names = []
        self.get_data()

    def get_data(self):
        response = requests.get(url=SHEET_API)
        response.raise_for_status()
        data = response.json()['prices']
        for city in data:
            self.city_names.append(city['city'])
            self.city_code[city['city']] = city['iataCode']
            self.city_lowest_price[city['city']] = city['lowestPrice']