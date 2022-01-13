# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Rich Whiffen - 1/12/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 3 - assignment 3.2 -
# reusing the stub from day 2

#BMI = int(float(weight) / (float(height)*float(height)))
# switching to the exponent ** operator
BMI = round((float(weight) / float(height)**2),1)

#Need both 1 decimal and no decimal :-/
whole_BMI = round(BMI)


if BMI < 18.5:
    print(f"Your BMI is {whole_BMI}, you are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print(f"Your BMI is {whole_BMI}, you have a normal weight.")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {whole_BMI}, you are slightly overweight,")
elif BMI >= 30 and BMI < 35:
    print(f"Your BMI is {whole_BMI}, you are obese.")
elif BMI >= 35:
    print(f"Your BMI is {whole_BMI}, you are clinically obese")

#originally I had a variable called "condition"
# that woudl be set and then you'd print you are {condition}
# but the different categories have different wording
