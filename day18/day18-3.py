# Rich Whiffen - 9/9/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 18 - more turtle graphics
#
# more loops - nesting two now.
#
# Ver 0.1
# Draw multi-side shapes.  Will start by drawing them on top of each
# other but should probably figure out some spacing to move them
# from each other.

from turtle import Turtle, Screen
import random


timmy = Turtle() #create a new turtle object
timmy.shape("turtle")

timmy.down()

shape_sides=3
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(sides):
    x=0
    angle=360/sides
    while x < sides:
        timmy.forward(100)
        timmy.right(angle)
        x += 1 # increment inner loop counter

while shape_sides < 11:

    draw_shape(shape_sides)
    shape_sides += 1 # increment outter loop.
    timmy.color(random.choice(colors))


my_screen = Screen() # create the Screen
my_screen.exitonclick()
