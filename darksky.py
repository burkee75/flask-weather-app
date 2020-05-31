"""Request:
 https://api.darksky.net/forecast/[key]/[latitude],[longitude]
"""

import requests 
from requests.exceptions import HTTPError, Timeout
from location import MapboxLocation
import sys 


class DarkSkyWeather:

    def __init__(self, darksky_api_key, mapbox_api_key, zipcode):
        self.darksky_api_key = darksky_api_key
        self.mapbox_api_key = mapbox_api_key
        self.zipcode = zipcode

    def get_forecast(self):
        """
        """
        location = MapboxLocation(self.mapbox_api_key)
        #print(location.latitude_longitude(self.zipcode))
        
        # have to reformat the latitude and longitude for NOAA request
        coordinates = f"{str(location.latitude_longitude(self.zipcode)[1])},{str(location.latitude_longitude(self.zipcode)[0])}"
        print(f'Formatted coordinates are: {coordinates}') #for degbugging

        url = f"https://api.darksky.net/forecast/{self.darksky_api_key}/{coordinates}"
        print(url)
        try:
            forecast_request = requests.get(url=url, timeout=5)
            forecast_request.raise_for_status()
            print(f"DarkSky Forecast Request HTTP Code: {forecast_request.status_code}") 
            return forecast_request.json()

        except Timeout:
            print("The request timed out...")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 
        except Exception as err:
            print(f'Other error occurred: {err}')
            sys.exit(1)   
 
    
