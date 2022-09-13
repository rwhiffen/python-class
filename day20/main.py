# Rich Whiffen - 9/13/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 20 - snake game and coordinates
#
# make the snake game.

from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_in_progress = True
while game_in_progress:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
