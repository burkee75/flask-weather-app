import json 
import sys

from icecream import ic
from mapbox import Geocoder
import requests
from requests.exceptions import HTTPError, Timeout

class Location:
    """
    Creates object for getting weather forecast from NOAA (weather.gov).
    Currently NOAA requires a User-Agent set in the headers but it can be literally anything.
    """

    def __init__(self):
        self.headers = {
            'User-Agent':'personal-project'
            }

    def location_as_lat_long(self, latitude, longitude):
        self.coordinates = [latitude, longitude]

    def location_as_zip(self, zipcode, api_key):
        geocoder = Geocoder(access_token=api_key)
        response = geocoder.forward(zipcode, country=['us'])
        ic({response.status_code})
        # Get Zipcode Center Latitude and Longitude from Mapbox
        ic(response.json()['features'][0]['center'])
        self.coordinates = response.json()['features'][0]['center']
   
    @property
    def forecast_zone(self):
        """To get the forecast we first have to find the Zone from NOAA"""

        try:
            r = requests.get(f'https://api.weather.gov/points/{self.coordinates[1]},{self.coordinates[0]}', headers=self.headers, timeout=5)
            r.raise_for_status()
            ic({r.status_code}) 
            forecast_request_url = r.json()['properties']['forecast']
            return forecast_request_url

        except Timeout:
            print("The request timed out...")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 
        except Exception as err:
            print(f'Other error occurred: {err}')
            sys.exit(1)   

    @property
    def weather_forecast(self):
        """
        Gets the Weather forecast summary from NOAA using the supplied URL. 
        URL must formatted as https://api.weather.gov/gridpoints/TFX/{ZONE}/forecast.
        Use the get_forecast_zone method to determine this.
        """

        try:
            forecast = requests.get(url = self.forecast_zone, headers=self.headers, timeout=5)
            forecast.raise_for_status()
            ic({forecast.status_code}) 
            return forecast.json()

        except Timeout:
            print("The request timed out...")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 
        except Exception as err:
            print(f'Other error occurred: {err}')
            sys.exit(1)   
