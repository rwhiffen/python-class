# Rich Whiffen - 9/10/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 18 - more turtle graphics
#
# more loops - introduction Tupples for colors
# also cleaningup the import AS to match the class
#



from turtle import Screen
from random import randint
import random
import turtle as t

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color_tuple=(r,g,b)
    return(color_tuple)


t.colormode(255) # set to RGB color question_mode

timmy = t.Turtle() #create a new turtle object
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
    timmy.color(random_color())
    walk_steps += 1

my_screen = Screen() # create the Screen
my_screen.exitonclick()
