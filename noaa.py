import json 
import requests
from requests.exceptions import HTTPError, Timeout
import sys

class NoaaWeather:
    """
    Creates object for getting weather forecast from NOAA (weather.gov).
    Currently NOAA requires a User-Agent set in the headers but it can be literally anything.
    """

    def __init__(self, coordinates):
        self.headers = {
            'User-Agent':'personal-project'
            }
        self.coordinates = coordinates

    def get_forecast_zone(self):
        """To get the forecast we first have to find the Zone from NOAA"""

        try:
            r = requests.get(f'https://api.weather.gov/points/{self.coordinates}', headers=self.headers, timeout=5)
            r.raise_for_status()
            print(f"Get Forecast Zone Request HTTP Code: {r.status_code}") 
            forecast_request_url = r.json()['properties']['forecast']
            return forecast_request_url

        except Timeout:
            print("The request timed out...")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 
        except Exception as err:
            print(f'Other error occurred: {err}')
            sys.exit(1)   


    def  get_weather_forecast(self):
        """
        Gets the Weather forecast summary from NOAA using the supplied URL. 
        URL must formatted as https://api.weather.gov/gridpoints/TFX/{ZONE}/forecast.
        Use the get_forecast_zone method to determine this.
        """

        try:
            forecast = requests.get(url = self.get_forecast_zone(), headers=self.headers, timeout=5)
            forecast.raise_for_status()
            print(f"Weather Forecast Request HTTP Code: {forecast.status_code}") 
            return forecast.json()

        except Timeout:
            print("The request timed out...")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 
        except Exception as err:
            print(f'Other error occurred: {err}')
            sys.exit(1)   

       