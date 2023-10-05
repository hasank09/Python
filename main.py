# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
import datetime as dt
from dateutil import parser
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

notification = NotificationManager()
# LONDON_CODE = 'LON'
data = DataManager()

date_today = dt.date.today()
city_from = 'London'
# city_to = data.city_names[0]
# city_to = 'Berlin'
for i in range(len(data.city_names)):
    city_to = data.city_names[i]
    if city_to != city_from:
        flight = FlightData(data, date_from=date_today, city_from=city_from, city_to=city_to)
        print(flight.lowes_fare_flight)
        from_city = flight.lowes_fare_flight['cityFrom']
        from_city_code = flight.lowes_fare_flight['cityCodeFrom']
        to_city = flight.lowes_fare_flight['cityTo']
        to_city_code = flight.lowes_fare_flight['cityCodeTo']
        current_price = flight.lowes_fare_flight['price']
        from_date = parser.parse(flight.lowes_fare_flight['route'][0]['local_departure']).date()
        to_date = parser.parse(flight.lowes_fare_flight['route'][-1]['local_departure']).date()

        if flight.is_lowest_fare_found():
            flight_price = flight.get_lowest_price_found()

            sms = f"Lowest-Price Alert! only ${flight_price} to fly from {from_city}-{from_city_code}" \
                  f" to {city_to}-{to_city_code}, " \
                  f"from {from_date} to {to_date}."
            print(sms)
            notification.send_sms(sms)
        else:
            print(f'no lowest fare found for {city_to} current price is {current_price} ')
    else:
        print('To and from city cant be same')
