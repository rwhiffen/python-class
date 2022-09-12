# Rich Whiffen - 9/12/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 19 - instances and event listeners
#
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
