from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score1, align='center', font=("Aria", 70, 'bold'))
        self.goto(100, 200)
        self.write(self.score2, align='center', font=("Aria", 70, 'bold'))

    def score_play1(self):
        self.score1 += 1
        self.update_score()

    def score_play2(self):
        self.score2 += 1
        self.update_score()

