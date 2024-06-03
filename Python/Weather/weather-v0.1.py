import requests
from geopy.geocoders import Nominatim
import json

# kelvin to farenheit
def ktof(K):
    f = ((K - 273.15) * 9) / 5 + 32
    return f


# OpenWeather api
API_KEY = "70de7df026e4b235bb56cdddec86442f"

# beginning process of converting user zip code to a lat/long format
# get current address from user, save as usradd
usradd = input("Address: ")
print("Searching...")

# object geolocater uses the Nominatim tool from the geopy module
geolocater = Nominatim(user_agent="Portfolio")
locinfo = geolocater.geocode(usradd)        # converting the user given address into a complete address, with full data
latlong = [str(locinfo.latitude), str(locinfo.longitude)] # save as lat long in list "latlong"

# creating API request
base_url = "https://api.openweathermap.org/data/3.0/onecall?"
complete_url = base_url + "lat=" + latlong[0] + "&lon=" + latlong[1] + "&appid=" + API_KEY

# perform request
print("Sending request...")
data = requests.get(complete_url)
print("Request recieved, processing...")
jdata = data.json()     # process json

# current temp in kelvin to ctempk; converting to farenheit as ctempc
ctempk = jdata['current']['temp']
ctempc = ktof(ctempk)

# feels like crealfeel
crealfeel = ktof(jdata['current']['feels_like'])

# current humidity = chumidity
chumidity = jdata['current']['humidity']

# description of current weather = cdesc
cdesc = jdata['current']['weather'][0]['description']

# display all current weather data in an easy to read format
print(f'Current Weather:\n'
      f'Temperature(F): {ctempc}\n'
      f'Feels Like:     {crealfeel}\n'
      f'Humidity:       {chumidity}\n'
      f'{cdesc}\n')