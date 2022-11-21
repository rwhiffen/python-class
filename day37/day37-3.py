# Rich Whiffen - 11/21/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 37 - working with APIs
#
# Figuring out how to do Auth examples.
# part 3 updating the graph and making it work
#

import requests
from datetime import datetime
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


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("1 for yes, I did python today, 0 for no python today"),
}


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


## PUT
response = requests.put(url=update_endpoint, json=pixel_data, headers=headers)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
