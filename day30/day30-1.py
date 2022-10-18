# Rich Whiffen - 10/17/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 30 - Exception Handling

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as index_error_message:
        print("fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)
