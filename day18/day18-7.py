# Rich Whiffen - 9/10/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 18 - more turtle graphics - chaleng 5 (I know file names are off)
#



from turtle import Screen
from random import randint
import random
import turtle as t

color_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205)]

t.colormode(255) # set to RGB color question_mode

timmy = t.Turtle() #create a new turtle object
timmy.shape("turtle")
timmy.pensize(5)
timmy.speed("fastest")
timmy.up()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

my_screen = Screen() # create the Screen
my_screen.exitonclick()
