from turtle import Turtle, Screen
import turtle
from random import randint

turtle.colormode(255)
t = Turtle()


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    random_color = (r, g, b)

    return random_color


def column():
    for _ in range(5):
        t.color(random_color())
        t.up()
        t.forward(100)
        t.dot(45)


def go_start_point():
    t.up()
    t.backward(300)
    t.right(90)
    t.forward(200)
    t.left(90)


def left_maneuver():
    t.left(90)
    t.forward(100)
    t.left(90)


def right_maneuver():
    t.right(90)
    t.forward(100)
    t.right(90)


def back_step_column():
    t.backward(100)
    column()


def first_column():
    go_start_point()
    column()


t.speed("fastest")
t.up()
first_column()
left_maneuver()
back_step_column()
right_maneuver()
back_step_column()
left_maneuver()
back_step_column()
right_maneuver()
back_step_column()

screen = Screen()
screen.exitonclick()
