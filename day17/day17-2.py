# Rich Whiffen - 9/9/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 17 - making our own classes
# part - 2 adding methods.
#
#
class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1 #add one to passed in user
        self.following += 1 #add one to my own following


user_1 = User("100", "Fred")


user_2 = User("101", "Barny")


print(" User - Followers - Following")
print(user_1.name, user_1.followers, user_1.following)
print(user_2.name, user_2.followers, user_2.following)


user_1.follow(user_2)
# this shoudl add 1 to user_1 following and 1 to user_2 followers
print(" User - Followers - Following")
print(user_1.name, user_1.followers, user_1.following)
print(user_2.name, user_2.followers, user_2.following)
