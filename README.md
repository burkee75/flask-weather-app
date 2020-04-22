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