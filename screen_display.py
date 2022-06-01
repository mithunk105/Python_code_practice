from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Display(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-280, 250)
        self.show_score()
        self.hideturtle()

    def show_score(self):
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
