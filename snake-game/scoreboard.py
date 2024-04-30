from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        with open("high_score.txt", mode="r") as high_score_txt:
            hst = high_score_txt.read()

        self.high_score = int(hst)
        self.score = 0
        self.death = 0

        self.up()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.write("Score: " + str(self.score) + " || High Score: " + str(self.high_score) + " || Deaths: " + str(self.death), align='center', font=('Arial', 15, 'bold'))

    def update_scoreboard(self):
        self.clear()
        self.write("Score: " + str(self.score) + " || High Score: " + str(self.high_score) + " || Deaths: " + str(self.death), align='center', font=('Arial', 15, 'bold'))

    def my_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score_txt:
                high_score_txt.write(str(self.high_score))
        self.score = 0
        self.death += 1
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
