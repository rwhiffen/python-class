# Rich Whiffen - 9/27/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 26 - list comprehension - convert C to F into a dictionary
#

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day:(temp_c*9/5+32) for (day, temp_c) in weather_c.items()}


print(weather_f)
