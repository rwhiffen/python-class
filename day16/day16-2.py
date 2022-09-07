# Rich Whiffen - 9/7/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 16-2 - intermediate OOP
#
# working with prettytable to make ascii tables - just more OOP practice
#

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="r"

print(table)
