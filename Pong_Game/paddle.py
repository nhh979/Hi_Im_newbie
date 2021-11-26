from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.goto(position)

    def up(self):
        self.fd(30)

    def down(self):
        self.bk(30)