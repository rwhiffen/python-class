# Rich Whiffen - 9/19/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 23 - Turtle-Crossing - Frogger/Crossy Road type game
#
# The class provided initial stubs to speed things up.
#



import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
