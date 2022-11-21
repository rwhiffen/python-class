# Rich Whiffen - 11/21/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 37 - working with APIs
#
# Figuring out how to do Auth examples.
# part 2 creating an graph - this code only works once. it will
# already be created if run twice
#

import requests
from secrets import secrets # store these outside the code

DEBUG=True

USERNAME = secrets['username']
TOKEN = secrets['token']
GRAPH_ID = secrets['id']
NAME = secrets['name']
TYPE = secrets['type']
UNIT = secrets['unit']
COLOR  = secrets['color']

if DEBUG:
    print(f"username: {USERNAME}")
    print(f"token: {TOKEN}")

pixela_endpoint =  "https://pixe.la/v1/users"


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": NAME,
    "unit": UNIT,
    "type": TYPE,
    "color": COLOR
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
