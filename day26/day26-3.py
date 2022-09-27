# Rich Whiffen - 9/27/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 26 - list comprehension - data overlap
#

with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [int(item) for item in list1 if item in list2]
# Write your code above 👆

print(result)
