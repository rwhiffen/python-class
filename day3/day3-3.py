# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Rich Whiffen - 1/12/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 3 - assignment 3.2 - is it a leap year?
# this was fun - had to get the else fall back logic to nest
# had a few fails because of typo type stuff - capital y on
# year, missing a period etc so it took me more tries that
# I would have expected to clear the codingrooms.com tests

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
