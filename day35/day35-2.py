# Rich Whiffen - 11/18/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 35 - working with APIs
#
# Working with APIs that need access tokens/Auth
#
# get the weather from the openweather API to start.
#

#Remember to x out before committing...
#should make a secrets.py and have a gitignore for that...


API_KEY="XXXXXXXXX"
DEBUG=True
it_will_rain = False #start out with no rain
import requests

parameters = {
    "lat" : 38.902660,
    "lon" : -77.032120,
    "exclude" :"current,minutely,daily",
    "appid" : API_KEY,
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
if DEBUG:
    print(weather_data["hourly"][0]["weather"][0])
weather_slice = weather_data["hourly"][:12]
if DEBUG:
    print(weather_slice)
for weather_hour in weather_slice:
    print(weather_hour["weather"][0]["id"]) #print the weather ID codes
    weather_cond = weather_hour["weather"][0]["id"]
    if int(weather_cond) < 700:
        it_will_rain = True

if it_will_rain:
    print("Bring an Umbrella")
