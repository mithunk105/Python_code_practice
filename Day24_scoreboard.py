from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highest_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}  Highest Score: {self.highest_score}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highest_score}")

        self.score = 0
        self.clear()
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()
