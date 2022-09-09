# Rich Whiffen - 9/9/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 18 - more turtle graphics - dashed line
# these are pretty easy so far - did logo programing back in the day.
#

from turtle import Turtle, Screen


timmy = Turtle() #create a new turtle object
timmy.shape("turtle")
timmy.color("blue")

line_length=0
line_draw=0
line_space=0

while line_length < 15:
    timmy.down()
    timmy.forward(10)
    timmy.up()
    timmy.forward(10)
    line_length += 1


my_screen = Screen() # create the Screen
my_screen.exitonclick()
