# README
This is a very basic personal weather website using Flask. 
Pulls weather from NOAA API while using MapBox to locate Latitude and Longitude coordinates.
I plan to keep working on this site as I learn other skills.

## Config.yaml
The config.yaml file holds the MapBox API key that needs to be provided.
The file should be formatted like so:

```yaml
---
# Configuration File for weather-app.py
mapbox_api:
  key: "<your-api-key-here>"
  ```

The file should be in the top level directory of the project. 

## Running the app
1. clone git repo
2. Create a config.yaml file. You will need a free API key from mapbox.com
3. pipenv install
4. pipenv shell
5. source env_setup.sh (this just sets environment variables)
6. flask run

If you open your browser to http://127.0.0.1:5000 you should get the webpage
