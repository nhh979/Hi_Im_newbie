from turtle import Turtle

start_position = [(0,0), (-20,0), (-40,0)]
class Snake():

    def __init__(self):
        self.body_snake = []
        self.create_snake()
        self.head = self.body_snake[0]

    def create_snake(self):
        for position in start_position:
            self.add_part(position)

    def add_part(self, position):
        hieu_snake = Turtle('square')
        hieu_snake.color("white")
        hieu_snake.penup()
        hieu_snake.goto(position)
        self.body_snake.append(hieu_snake)

    def get_larger(self):
        self.add_part(self.body_snake[-1].position())

    def move(self):
        for part_position in range(len(self.body_snake) - 1, 0, -1):
            new_position = part_position - 1
            new_xcor = self.body_snake[new_position].xcor()
            new_ycor = self.body_snake[new_position].ycor()
            self.body_snake[part_position].goto(new_xcor, new_ycor)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
