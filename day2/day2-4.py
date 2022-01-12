# Rich Whiffen - 1/11/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 2 - assignment 2.5
# Tip calculator free-for excersize

print("Welcome to the tip calculator")
# convert string to float on input - this should
# probably not be done and test for valid numbers
# but we're just learning here
bill = float(input("What was the total bill? "))

# going to concat the string first then float() it
base_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
#prepend a 1. to make it easier math
perc_tip = float("1."+base_tip)

#  convert string to int on input rather than a temp string
num_people = int(input("how many people to split the bill? "))

#I may commment this out later and make it a one liner...
total_bill = bill * perc_tip
per_person = round(total_bill / num_people, 2)

print(f"Each person should pay: ${per_person}")
