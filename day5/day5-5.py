# Rich Whiffen - 1/27/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# day 5 assignment 5.5  - Random password generator
#
#starter code from replit:
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#password=""
#
#for letter_pick in range(1,nr_letters+1):
#    password+=random.choice(letters)
#
#for symbol_pick in range(1,nr_symbols+1):
#    password+=random.choice(symbols)
#
#for number_pick in range(1,nr_numbers+1):
#    password+=random.choice(numbers)
#
#print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# the hard part:

password_list=[]
password="" # set it to a string type
for letter_pick in range(1,nr_letters+1):
    password_list+=random.choice(letters)

for symbol_pick in range(1,nr_symbols+1):
    password_list+=random.choice(symbols)

for number_pick in range(1,nr_numbers+1):
    password_list+=random.choice(numbers)

random.shuffle(password_list) # scramble the list

for character in password_list:
    password += character
print(f"your password is: {password}")
