import googlemaps
# from datetime import datetime
# import json


def decodeLocation():
    userLocation = input("Enter city: ")
    if isinstance(userLocation, str):
        pass
    else:
        raise TypeError('Input must be a string')

    gmaps = googlemaps.Client(key='AIzaSyAEvGEWpDcLpr4BpDomcQbxm7JkqyR51Gg')
# Geocoding an address
    geocode_result = gmaps.geocode(userLocation, {"country": "KE"})
    result = geocode_result[0]['geometry']['location']
    places_nearby = gmaps.places('Hospital', result, 500)
    print(places_nearby)


decodeLocation()
# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
