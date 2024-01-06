
from options_reader import OptionsReader
from request_sender import RequestSender
from data_parser import DataParser
from data_writer import DataWriter


fields = ['last_updated',
            'temp_c',
            'cloud',
            'humidity',
            'wind_kph'
            ]

cities = OptionsReader.read_cities('cities.yaml')
weather_data = []

for city in cities:
    response = RequestSender.send_request(city)
    data = DataParser.parse(response, fields)
    weather_data.append(data)

headers = ['city'] + fields

DataWriter.write2csv('weather.csv', headers=headers, data=weather_data)
