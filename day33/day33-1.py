# Rich Whiffen - 11/9/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 33 - working with APIs
#
# simple request & response - ISS position

import requests #pip3 install requests
DEBUG = True

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() #raise the actual excetpion
print(response)

#example of directly handling the status_code
if response.status_code == 404:
    raise Exception("Whoops 404; URL typo?")
elif response.status_code == 403:
    raise Exception("Whoops 403; denied - login?")
elif response.status_code > 499:
    raise Exception("got a 5xx")

raw_data = response.json()
if DEBUG:
    print(raw_data)
latitude = raw_data["iss_position"]["latitude"]
longitude = raw_data["iss_position"]["longitude"]
iss_position = (latitude, longitude)

if DEBUG:
    print(f"ISS Position: {iss_position}")
