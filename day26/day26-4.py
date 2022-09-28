# Rich Whiffen - 9/27/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 26 - list comprehension - get the words and lengths in a dictionary
#
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {word:len(word) for word in sentence.split()}

print(result)
