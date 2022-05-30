from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import Ball
from paddle_score_board import PaddleScore
import time


def draw_line_vertically():
    tim = Turtle()
    tim.color("white")
    tim.left(90)
    tim.penup()
    tim.forward(300)
    tim.setheading(270)
    for _ in range(60):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

draw_line_vertically()


lpaddle = Paddle((-350, 0))
rpaddle = Paddle((350, 0))
ball = Ball()
score = PaddleScore()

screen.listen()
screen.onkey(fun=rpaddle.go_up, key="Up")
screen.onkey(fun=rpaddle.go_down, key="Down")
screen.onkey(fun=lpaddle.go_up, key="w")
screen.onkey(fun=lpaddle.go_down, key="s")

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.on_collision_wall()

    if ball.distance(rpaddle) < 50 and ball.xcor() > 321 or ball.distance(lpaddle) < 50 and ball.xcor() < -321:
        ball.on_collision_paddle()

    if ball.xcor() > 380:
        ball.reset_ball()
        score.left_score()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.right_score()


screen.exitonclick()
