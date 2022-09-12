# Rich Whiffen - 9/12/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 19 - instances and event listeners
#
from turtle import Turtle, Screen

#Set the move and angle variables globally

GLOBAL_MOVE=10
GLOBAL_HEADING=10

def move_forwards():
    timmy.forward(GLOBAL_MOVE)

def move_backwards():
    timmy.backward(GLOBAL_MOVE)

def turn_left():
    new_heading = timmy.heading() + GLOBAL_HEADING
    timmy.setheading(new_heading)

def turn_right():
    new_heading = timmy.heading() - GLOBAL_HEADING
    timmy.setheading(new_heading)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


timmy = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
