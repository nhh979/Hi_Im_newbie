from turtle import Turtle

font_write = ("Courier", 25 ,"italic")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("White")
        self.update_score()

    def add_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=font_write)

    def game_over(self):
        self.home()
        self.color('white')
        self.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
