# Rich Whiffen - 2/7/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 8 - assignment 8.2 - paint can function.
#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    cans = math.ceil((height * width) / cover)
    print(f"You'll need {cans} cans of paint.")




#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
