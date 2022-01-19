# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Rich Whiffen - 1/18/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 3 - assignment 3.4 - pizza order
# had to take a few days off

#Get the base costs based on size.
if size == "S":
    cost=15
elif size == "M":
    cost=20
else:
    cost=25
#defaults to 25 - there's no error checking here :-/
#I wonder if python has a to-upper function to normalize case...

if add_pepperoni == "Y" and size == "S":
    cost+=2
if add_pepperoni == "Y" and size == "M":
    cost+=3
if add_pepperoni == "Y" and size == "L":
    cost+=3

#those to could be a single one - add && (M or L) - figure that out some day

if extra_cheese == "Y":
    cost+=1

print (f"Your final bill is: ${cost}.")
