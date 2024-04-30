from turtle import Screen
from super_turtle import SuperTurtle, Window

window = Window()
window.mainloop()

screen = Screen()
screen.setup(600, 600)
t = SuperTurtle()

screen.listen()
screen.onkeypress(t.move_forward, "Up")
screen.onkeypress(t.turn_right, "Right")
screen.onkeypress(t.turn_left, "Left")
screen.onkeypress(t.put_dot, "space")

screen.exitonclick()