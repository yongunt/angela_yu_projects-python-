import random
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False

n = 200
c = -1
for _ in range(6):
    n -= 50
    c += 1
    t = Turtle(shape="turtle")
    t.color(colors[c])
    t.up()
    t.goto(x=-230, y=n)
    all_turtles.append(t)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} win the race!")
                is_race_on = False
            else:
                print(f"You've lost! The {wining_color} win the race!")
                is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
