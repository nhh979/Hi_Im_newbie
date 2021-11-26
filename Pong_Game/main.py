from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
from random import randint
import math
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

user1 = Paddle((-350, 0))
user2 = Paddle((350, 0))

screen.listen()
screen.onkey(user1.up, "w")
screen.onkey(user1.down, "s")
screen.onkey(user2.up, "Up")
screen.onkey(user2.down, "Down")

ball = Ball()
score = Scoreboard()

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(0.01)

    if ball.xcor() > 400:
        score.score_play1()
        ball.start_point(randint(120, 240))

    if ball.xcor() < -400:
        score.score_play2()
        ball.start_point(randint(-60, 60))

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()

    if (ball.xcor() >=330 or ball.xcor() <= -330) and (ball.distance(user1) < math.sqrt(2900) or ball.distance(user2) < math.sqrt(2900)):
        ball.paddle_bounce()
        ball.increase_speed()

screen.exitonclick()