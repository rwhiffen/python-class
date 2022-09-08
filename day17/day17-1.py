# Rich Whiffen - 9/7/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 17 - making our own classes
#
#
class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0


    pass

user_1 = User("100", "Fred")

print(user_1.id, user_1.name)

user_2 = User("101", "Barny")

print(user_2.name, user_2.followers)
