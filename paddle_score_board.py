from turtle import Turtle


class PaddleScore(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.lscore = 0
        self.rscore = 0
        self.penup()
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.goto(-100, 200)
        self.write(f"{self.lscore}", align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.rscore}", align="center", font=("Courier", 80, "normal"))

    def left_score(self):
        self.clear()
        self.lscore += 1
        self.show_score()

    def right_score(self):
        self.clear()
        self.rscore += 1
        self.show_score()







