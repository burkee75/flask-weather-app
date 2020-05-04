# Weather App powered by Flask
import json
import sys 

from flask import Flask, render_template, request, redirect, url_for
import requests
from requests.exceptions import HTTPError, Timeout
import yaml

from forms import ZipcodeForm
from location import Location

app = Flask(__name__)
app.config['SECRET_KEY'] = 'alsdfhaohgawior2103494'

with open('config.yaml', 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = ZipcodeForm()

    if request.method == 'POST':
    #if form.validate_on_submit():
        if form.validate():
            zipcode = form.zipcode.data
            print(f'\nYou entered: {zipcode}\n')

            location = Location()
            location.location_as_zip(zipcode, config['mapbox_api']['key'])
            tomorrow_summary = location.weather_forecast['properties']['periods'][2]['shortForecast']
            print(f"Tomorrow's Forecast is: {tomorrow_summary}")

            return render_template("weather.html", result = tomorrow_summary)
        else:
            return render_template('home.html', form=form)


    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
