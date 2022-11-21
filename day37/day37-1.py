# Rich Whiffen - 11/21/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 37 - working with APIs
#
# Figuring out how to do Auth examples.
# part 1 creating an account - this code only works once.
#

import requests
from secrets import secrets # store these outside the code

pixela_endpoint =  "https://pixe.la/v1/users"

response = requests.post(url=pixela_endpoint, json=secrets)

print (response.text)
