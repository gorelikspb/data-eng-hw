import requests
import json

class RequestSender:
    API_KEY = 'c55e0f5cb6d44325ae7184912240601'

    @staticmethod
    def send_request(city):
        url = (
            f'http://api.weatherapi.com/v1/'
            f'current.json?key={RequestSender.API_KEY}&'
            f'q={city}'
            )
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print('Request error', response.status_code)


if __name__ == "__main__":
    print(RequestSender.send_request('Saint-Petersburg'))