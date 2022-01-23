import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Rich Whiffen - 1/22/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 4 - assignment 4.2 - Banker Roulette
#
# the seed makes the first random fuction predictable which is why it's used
# the tests will pass in the codingroom.com assignment then
#
max_names = len(names)
#print(f"{max_names}")
# have to take one off of max_names to get the zero to X to align.
pick = random.randint(0,(max_names - 1))
#print(f"{pick}")
print(f"{names[pick]} is going to buy the meal today!")
