import requests

TEQUILA_API = 'U6OXasWOQmJ_EejCjv56vVxf5y7p6tio'
FLIGHT_ENDPOINT = 'https://api.tequila.kiwi.com/v2/search'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.header = {'apikey': TEQUILA_API, }

    def search_flight(self, city_from, city_to, date_from, date_to):
        parameter = {
            'fly_from': city_from,
            'fly_to': city_to,
            'date_from': date_from,
            'date_to': date_to,
            'flight_type': 'round',
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            "one_for_city": 1,
            'curr': 'USD',
            'limit': 10,
        }
        response = requests.get(url=FLIGHT_ENDPOINT, params=parameter, headers=self.header)
        response.raise_for_status()
        data = response.json()
        result = data['data']
        # print(data['search_params']['seats'])
        # print(result)
        # for data in result:
        #     price = data['price']
        #
        #     print(price)
        return result


