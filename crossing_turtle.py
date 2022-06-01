from turtle import Turtle


class CTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.reset()

    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(0, -280)
