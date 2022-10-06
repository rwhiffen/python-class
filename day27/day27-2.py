# Rich Whiffen - 10/04/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 27 - kwargs and args - passing arbitrary args and keyword args.

# *args: Positional Variable-Length Arguments
def add(*args):
    # print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum

print("*args ")
print(add(3, 5, 6, 2, 1, 7, 4, 3))
print("*args ")


# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
