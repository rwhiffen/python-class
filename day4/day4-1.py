#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.

#Write the rest of your code below this line 👇
# Rich Whiffen - 1/19/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 3 - assignment 4.1 - Even or Odd
# the seed makes the first random fuction predictable which is why it's used
# the tests will pass then
#
flip = random.randint(0,1)
if (flip == 0 ):
    print('heads')
else:
    print('tails')
