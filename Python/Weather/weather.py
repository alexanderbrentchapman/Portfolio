import requests
from geopy.geocoders import Nominatim
import json

# OpenWeather api
API_KEY = "70de7df026e4b235bb56cdddec86442f"

# beginning process of converting user zip code to a lat/long format
# get current address from user, save as usradd
#usradd = input("Address: ")
#print("Searching...")
usradd = "609 aspen lane edgewood maryland" # for quick debug purposes. remove this line for final product

# object geolocater uses the Nominatim tool from the geopy module
geolocater = Nominatim(user_agent="Portfolio")
locinfo = geolocater.geocode(usradd)        # converting the user given address into a complete address, with full data
latlong = [str(locinfo.latitude), str(locinfo.longitude)] # save as lat long in list "latlong"

# creating API request
base_url = "https://api.openweathermap.org/data/3.0/onecall?"
complete_url = base_url + "lat=" + latlong[0] + "&lon=" + latlong[1] + "&appid=" + API_KEY

# get method of requests module
# return response object
response = requests.get(complete_url)

# json of response
# convert json into python list, dictionaries
data = response.json()

print(data)

