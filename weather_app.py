# Weather App powered by Flask

from flask import Flask, render_template, request
import json
import requests
from requests.exceptions import HTTPError, Timeout
import sys 
import yaml
from darksky import DarkSkyWeather
import datetime


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


        mapbox_api_key = "pk.eyJ1IjoiYmlnc2t5dGVjaC1pbyIsImEiOiJjazNnOTc5eWowMGFpM2ZvY29rMmdvOWFtIn0.iAMSXmKVw5tkgf-h8Wu9hg"
        #mapbox_api_key = config['mapbox_api']['key'] #for loading from yaml

        darksky_api_key = "f43b221728bcd8e941b70eb5c7d125cf"
        #darksky_api_key = config['mapbox_api']['key'] #for loading from yaml. need to add to config.yaml

        weather_request = DarkSkyWeather(darksky_api_key, mapbox_api_key, zipcode).get_forecast()
        #print(forecast.get_forecast())
        #         
        current_temp = weather_request['currently']['temperature']
        print(f"Current Temp is: {current_temp}")

        daily_summary = weather_request['daily']['data']
        for day in daily_summary:
            #print(f" Date: {datetime.datetime.fromtimestamp(day['time']).strftime('%m-%d-%Y')}, Summary: {day['summary']}")
            unixtime = day['time']
            day['time'] = datetime.date.fromtimestamp(unixtime).strftime('%A, %B %d')
            print(f'Changed {unixtime} to {day["time"]}')
        #tomorrow_summary = weather.get_weather_forecast()['properties']['periods'][2]['shortForecast']
        #print(f"Tomorrow's Forecast is: {tomorrow_summary}")

        #forecast_list = weather.get_weather_forecast()['properties']['periods']
        #print(forecast_list)

        #for day in forecast_list:
        #    #for key, value in day.items():
        #        #print(f'{key}, {value}')
        #    print(f"{day['name']}: {day['shortForecast']}")


        return render_template("weather.html", current_temp=current_temp, daily_summary=daily_summary)


if __name__ == '__main__':
    app.run(debug=True)
