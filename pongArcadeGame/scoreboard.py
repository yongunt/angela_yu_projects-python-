from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.goto(-170, 230)
        self.write(self.l_score, font=("Arial", 50, "bold"))
        self.goto(140, 230)
        self.write(self.r_score, font=("Arial", 50, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.goto(-170, 230)
        self.write(self.l_score, font=("Arial", 50, "bold"))
        self.goto(140, 230)
        self.write(self.r_score, font=("Arial", 50, "bold"))

