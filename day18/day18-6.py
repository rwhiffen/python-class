# Rich Whiffen - 9/10/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 18 - more turtle graphics - chaleng 5 (I know file names are off)
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


def draw_spiro(slices, radius):
    for _ in range(int(350/slices)):
        timmy.color(random_color())
        timmy.circle(radius)
        timmy.setheading(timmy.heading()+slices) #rotate him +{slices}

t.colormode(255) # set to RGB color question_mode

timmy = t.Turtle() #create a new turtle object
timmy.shape("turtle")
timmy.pensize(5)
timmy.speed("fastest")
#timmy.down()

draw_spiro(5,100)
