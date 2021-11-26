from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.setheading(random.choice([i for i in range(-45, 45)] + [i for i in range (135, 225)]))
        self.ball_speed = 3

    def move(self):
        self.forward(self.ball_speed)

    def increase_speed(self):
        self.ball_speed += 1

    def start_point(self, direction):
        self.home()
        self.ball_speed = 3
        self.setheading(direction)

    def wall_bounce(self):
        self.setheading(360 - self.heading())

    def paddle_bounce(self):
        self.setheading(180 - self.heading())
