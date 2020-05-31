from darksky import DarkSkyWeather
import datetime

#self, darksky_api_key, mapbox_api_key, zipcode

mapbox_api_key = "pk.eyJ1IjoiYmlnc2t5dGVjaC1pbyIsImEiOiJjazNnOTc5eWowMGFpM2ZvY29rMmdvOWFtIn0.iAMSXmKVw5tkgf-h8Wu9hg"
darksky_api_key = "f43b221728bcd8e941b70eb5c7d125cf"

weather_request = DarkSkyWeather(darksky_api_key, mapbox_api_key, '59714').get_forecast()
#print(forecast)
current_temp = weather_request['currently']['temperature']
print(f"Current Temp is: {current_temp}")
daily_summary = weather_request['daily']['data']
#for day in daily_summary:
#    print(f" Date: {datetime.datetime.fromtimestamp(day['time']).strftime#('%m-%d-%Y')}, Summary: {day['summary']}")
for day in daily_summary:
    #print(f" Date: {datetime.datetime.fromtimestamp(day['time']strftime('%m-%d-%Y')}, Summary: {day['summary']}")
    unixtime = day['time']
    day['time'] = datetime.date.fromtimestamp(unixtime).strftime('%A, %B %d')
    print(f'Changed {unixtime} to {day["time"]}')

for day in daily_summary:
    print(f" Date: {day['time']}, Summary: {day['summary']}")