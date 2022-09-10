# Rich Whiffen - 9/9/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 18 - more turtle graphics
#
# more loops - nesting two now.
#
# Ver 0.1
# random walk

from turtle import Turtle, Screen
from random import randint
import random


timmy = Turtle() #create a new turtle object
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")
timmy.down()

walk_length = 200
walk_steps=0
walk_sides = 4 # grid walk
angle=0 #init

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def take_walk(angle):
        timmy.forward(30)
        timmy.setheading(angle) #changed to setheading instead of right - faster

while walk_steps < walk_length:

    turn=randint(1, walk_sides) # which direction to turn
    # class solution did it differently - but they both work.
    angle=(360/walk_sides) * turn # calc angle and multiply by random turn amount
    take_walk(angle)
    timmy.color(random.choice(colors))
    walk_steps += 1

my_screen = Screen() # create the Screen
my_screen.exitonclick()
