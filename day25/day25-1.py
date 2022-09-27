# Rich Whiffen - 9/23/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 25 - read a CSV file -
#
import csv


DEBUG=True


with open("weather_data.csv", "r") as weather_csv:
    weather_data = csv.reader(weather_csv)

    temperature = []
    for row in weather_data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)
