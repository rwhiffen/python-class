# Rich Whiffen - 11/21/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 38 - working with more APIs - I'm skipping the sheetly thing.  
#



import requests
from datetime import datetime
from secrets import secrets # store these outside the code

DEBUG=True


TOKEN = secrets['token']
APPID = secrets['appId']
GENDER = secrets['gender']
WEIGHT_KG = secrets['weightKg']
HEIGHT_CM = secrets['heightCm']
AGE = secrets['age']

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("What exercises did you do: ")

headers = {
    "x-app-id": APPID,
    "x-app-key": TOKEN,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
