# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# Rich Whiffen - 1/22/2022
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 4 - assignment 4.3 - treasure map
# mutli-dimensional arrays/lists
column = int(position[0]) - 1
row = int(position[1]) - 1
# -1 to handle zero relative.

map[row][column] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
