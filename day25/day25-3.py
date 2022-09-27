# Rich Whiffen - 9/23/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 25 - read a CSV file - using pandas
#

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
