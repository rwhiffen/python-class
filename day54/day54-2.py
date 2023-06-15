# Rich Whiffen - 6/14/2023
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 54 - FLASK with Python
#

# decorators

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/rich")
def say_rich_nest():
    return "outer nest"



if __name__ == "__main__":
    app.run()