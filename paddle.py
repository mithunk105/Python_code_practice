from turtle import Turtle
JUMP = 20


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(pos)

    def go_up(self):
        ycord = self.ycor() + JUMP
        self.goto(self.xcor(), ycord)

    def go_down(self):
        ycord = self.ycor() - JUMP
        self.goto(self.xcor(), ycord)
