# Rich Whiffen - 9/19/2022
#
# Udemy 100 Days of Code: The complete Python Pro Bootcamp for 2022
# Day 22 - PONG - most of this code is typed along with the lectures so
# not much original thought here.
# the paddle bounce isn't very good - sometimes the ball sticks to the paddle 
#
# make the snake game.


from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#init screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

#init paddles, score and ball
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

#start the listeners
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

#start the main loop
while game_is_on:
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # exit at 5 points - needs a "game over" graphic
    if scoreboard.l_score > 4 or scoreboard.r_score > 4:
        game_is_on = False

screen.exitonclick()
