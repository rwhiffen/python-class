# Rich Whiffen - 2/26/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 10 - assignment 10.1 - Student grades
# workign functions and returning values - took a few days off here...

# functions with output - just a simple function call to
# get started with the idea.

def format_name(f_name, l_name):
  format_name = f_name.title() + " " + l_name.title()
  return format_name

first_name= input("First Name: ").lower()
last_name = input("Last Name: ").lower()

print(f" {first_name} {last_name}")
full_name = format_name(first_name, last_name)
print(f" {full_name}")
