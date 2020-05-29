from mapbox import Geocoder

class MapboxLocation:

    def __init__(self, api_key):
        self.api_key = api_key
        self.geocoder = Geocoder(access_token=self.api_key)


    def latitude_longitude(self, zipcode):
        self.zipcode = zipcode
        response = self.geocoder.forward(self.zipcode, country=['us'])
        #print(f'Mapbox Zipcode Lookup HTTP code: {response.status_code}')
        # Get Zipcode Center Latitude and Longitude from Mapbox
        #print(f"Mapbox Coordinates: {response.json()['features'][0]['center']}") # for debugging

        return response.json()['features'][0]['center']
   
