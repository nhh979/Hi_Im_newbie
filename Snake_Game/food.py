from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.color('purple')
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))