# Rich Whiffen - 9/9/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 18 - more turtle graphics
#

from turtle import Turtle, Screen


timmy = Turtle() #create a new turtle object
timmy.shape("turtle")
timmy.color("blue")
timmy.down()

x=0
while x < 4:
    timmy.forward(100)
    timmy.right(90)
    x += 1


my_screen = Screen() # create the Screen
my_screen.exitonclick()
