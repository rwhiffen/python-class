# Rich Whiffen - 2/7/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 8 - assignment 8.1 - more with functions
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet( yourName ):
  print(f"Hi {yourName}")
  print("howdy")
  print("good day")

greet("blarg")

# the next one was to use two inputs
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"how is the weather in {location}")

greet_with("Rich", "Arlington")

greet_with(location="texas", name="blart")
