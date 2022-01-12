# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Rich Whiffen - 1/11/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 2 - assignment 2.3


end_date = 90 # die when we hit 90
years_left = end_date - int(age)

days= years_left * 365 #we're punting on leap years here
weeks = years_left * 52
months = years_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
