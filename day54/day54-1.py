# Rich Whiffen - 6/09/2023
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 54 - FLASK with Python
#
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

