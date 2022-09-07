# Rich Whiffen - 9/7/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 16-1 - intermediate OOP
#
# working with the turtle object - just following along with the lecture
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

#I think the instruction are wrong here - seems like I should be
#using the screen associated with the turtle object creation

my_screen = Screen() # create the Screen
my_screen.setup(width=300, height=300, startx=0, starty=0)
my_screen.bgcolor("white") # for some reason it defaults to black on my imac
my_screen.exitonclick()  # leave the screen up until I click it.
