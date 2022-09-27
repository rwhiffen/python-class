# Rich Whiffen - 9/23/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 25 - read a CSV file - using pandas
#

import pandas

data = pandas.read_csv("weather_data.csv")
#print(data["temp"])

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

#calling sub functions
print(data["temp"].mean())
print(data["temp"].max())

# you can call column names as attributes
print(data.condition)

# selecting rows
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])
