import turtle as t
import random


t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)

    return random_color


t.speed(10000000000000000000000*10000000000000000000000)

count = 0

while count < 3000:
    count += 1
    t.color(random_color())
    t.circle(100)
    t.left(5)



# count = 0
# while count < 51:
#     count += 1
#     if (-200 < turtle.xcor() < 200) and (-200 < turtle.ycor() < 200):
#         turtle.color(random_color())
#         turtle.right(random.randint(0, 360))
#         distance = random.randint(30, 100)
#         turtle.forward(distance)
#     else:
#         turtle.color(random_color())
#         turtle.right(random.randint(0, 180))
#         distance = random.randint(30, 100)
#         turtle.forward(distance)


screen = t.Screen()
screen.exitonclick()
