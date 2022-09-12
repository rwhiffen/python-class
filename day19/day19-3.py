# Rich Whiffen - 9/12/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 19 - instances and event listeners
#
# turtle race - initially I had hard-coded individual turtles and y coordinates
# refactored to match the class example. in hindsight I should have
# committed the initial space.

from turtle import Turtle, Screen
import random

DEBUG=False #speeds the  blue turtle so you know who wins

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True


while race_is_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        #turtles move in index order - turtle 0 will always move before 5
        if turtle.xcor() > 230:
            race_is_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
        if DEBUG:
            if turtle.pencolor() == "blue":
                turtle.forward(3) # give blue a boost

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
