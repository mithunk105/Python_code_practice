from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xcord = 10
        self.ycord = 10
        self.ball_speed = 0.1

    def move(self):
        xcord = self.xcor() + self.xcord
        ycord = self.ycor() + self.ycord
        self.goto(xcord, ycord)

    def on_collision_wall(self):
        self.ycord *= -1

    def on_collision_paddle(self):
        self.xcord *= -1
        self.ball_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.xcord *= -1
        self.ball_speed = 0.1
