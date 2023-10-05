# This class is responsible for structuring the flight data.
import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch


class FlightData:
    def __init__(self, data: DataManager, date_from, city_from, city_to):
        self.data = data
        self.date_from = date_from
        self.city_from = city_from
        self.city_to = city_to
        self.flight_data = FlightSearch()
        self.lowes_fare_flight = self.get_fare_flight()

    def get_fare_flight(self):
        # flight_data = FlightSearch()
        date_from = self.date_from.strftime('%d/%m/%Y')
        date_to = (self.date_from + dt.timedelta(days=30 * 6)).strftime('%d/%m/%Y')

        if (self.city_from in self.data.city_names) & (self.city_to in self.data.city_names):
            city_from_iata = self.data.city_code[self.city_from]
            city_to_iata = self.data.city_code[self.city_to]
            flight_data = self.flight_data.search_flight(city_from=city_from_iata, city_to=city_to_iata,
                                                         date_from=date_from, date_to=date_to)
            # print(flight_data[0])
            return flight_data[0]
        else:
            raise Exception('No City Found or no IATA exist for From/To City')

    def is_lowest_fare_found(self):
        new_lowes_price = self.lowes_fare_flight['price']
        my_lowest_price = self.data.city_lowest_price[self.city_to]

        if new_lowes_price < my_lowest_price:
            return True
        else:
            return False

    def get_lowest_price_found(self):

        return self.lowes_fare_flight['price']
