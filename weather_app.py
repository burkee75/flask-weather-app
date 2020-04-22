# Weather App powered by Flask

from flask import Flask, render_template, request
import json
import requests
from requests.exceptions import HTTPError, Timeout
import sys 
import yaml
from mapbox import Geocoder

app = Flask(__name__)

with open('config.yaml', 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/weather", methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        # uncomment this to use the form
        location = request.form['location']
        print(f'\nYou entered: {location}\n')

        #hard code location for testing
        #location = "45.783950,-111.176300"

        # MapBox Geocoder Lookup
        geocoder = Geocoder(access_token=config['mapbox_api']['key'])
        response = geocoder.forward(location, country=['us'])
        print(f'Mapbox Zipcode Lookup HTTP code: {response.status_code}')

        # Get Zipcode Center Latitude and Longitude from Mapbox
        lat_long = response.json()['features'][0]['center']
        print(f'Mapbox Coordinates: {lat_long}') # for debugging

        coordinates = f"{str(response.json()['features'][0]['center'][1])},{str(response.json()['features'][0]['center'][0])}"
        print(f'Formatted coordinates are: {coordinates}') #for degbugging

        # First get forecast zone, then get forecast

        headers = {
            'User-Agent':'personal-project'
            }
        try:
            zone_url = requests.get(f'https://api.weather.gov/points/{coordinates}', headers=headers, timeout=5)
            zone_url.raise_for_status()
            print(f"Weather Request HTTP Code: {zone_url.status_code}") 
        except Timeout:
            print("The request timed out...")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 
        except Exception as err:
            print(f'Other error occurred: {err}')
            sys.exit(1)   
        forecast_request = zone_url.json()['properties']['forecast']

        try:
            forecast = requests.get(forecast_request, headers=headers, timeout=5)
            forecast.raise_for_status()
            print(f"Weather Request HTTP Code: {forecast.status_code}") 
        except Timeout:
            print("The request timed out...")
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 
        except Exception as err:
            print(f'Other error occurred: {err}')
            sys.exit(1)   

        tomorrow_summary = forecast.json()['properties']['periods'][2]['shortForecast']
        print(f"Tomorrow's Forecast is: {tomorrow_summary}")
        return render_template("weather.html", result = tomorrow_summary)


if __name__ == '__main__':
    app.run(debug=True)
