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

import requests

parameters = {
    "lat" : 38.902660,
    "lon" : -77.032120,
#    exclude={part},
    "appid" : API_KEY,
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
print(response.json())
