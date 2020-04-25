# Weather App powered by Flask

from flask import Flask, render_template, request
import json
import requests
from requests.exceptions import HTTPError, Timeout
import sys 
import yaml
from location import Location
from noaa import NoaaWeather


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
        zipcode = request.form['location']
        print(f'\nYou entered: {zipcode}\n')

        location = Location(config['mapbox_api']['key'])
        print(location.latitude_longitude(zipcode))
        
        # have to reformat the latitude and longitude for NOAA request
        coordinates = f"{str(location.latitude_longitude(zipcode)[1])},{str(location.latitude_longitude(zipcode)[0])}"
        print(f'Formatted coordinates are: {coordinates}') #for degbugging

        # Get weather forecast
        weather = NoaaWeather(coordinates) #returns json
        #print(weather.get_weather_forecast())

        tomorrow_summary = weather.get_weather_forecast()['properties']['periods'][2]['shortForecast']
        print(f"Tomorrow's Forecast is: {tomorrow_summary}")

        return render_template("weather.html", result = tomorrow_summary())


if __name__ == '__main__':
    app.run(debug=True)
