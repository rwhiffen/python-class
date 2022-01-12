# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Rich Whiffen - 1/11/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 2 - assignment 2.2

#BMI = int(float(weight) / (float(height)*float(height)))
# switching to the exponent ** operator
BMI = int(float(weight) / float(height)**2)

print(str(BMI))
