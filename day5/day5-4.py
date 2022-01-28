#Write your code below this row 👇

# Rich Whiffen - 1/27/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# day 5 assignment 5.4  -  Fizbuzz simulation
#
# this is a useful intro to multi-indents.
# whitespace is going to be an issue in my future I can tell
for number in range(1,101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
       print("Buzz")
    else:
        print(number)
