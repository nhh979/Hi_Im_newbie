from turtle import  Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
list_turtle = []
y = -70

for color in colors:
    hieu_turtle = Turtle(shape="turtle")
    hieu_turtle.color(color)
    hieu_turtle.penup()
    hieu_turtle.goto(-230, y)
    list_turtle.append(hieu_turtle)
    y += 30

hieu_turtle.speed('fastest')
is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in list_turtle:
        random_step = random.randint(0, 10)
        turtle.forward(random_step)
        if turtle.xcor() >= 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You win. The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f'You lose. The {turtle.pencolor()} turtle is the winner!')

screen.exitonclick()