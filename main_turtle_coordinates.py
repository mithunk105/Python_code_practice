import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle color will win the race? Enter a color: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
yc = -150
obj_list = []
for i in range(0, len(colours)):
    tim = t.Turtle()
    tim.color(colours[i])
    tim.shape("turtle")
    tim.penup()
    yc += 50
    tim.goto(x=-230, y=yc)
    obj_list.append(tim)

is_race_on = False
if user_bet:
    is_race_on = True


while is_race_on:
    for tom in obj_list:
        tom.forward(random.randint(0, 10))
        if tom.xcor() >= 230:
            is_race_on = False
            win_color = tom.pencolor()
            if user_bet == win_color:
                print(f"You won! The {win_color} turtle is winner!")
            else:
                print(f"You lost! The {win_color} turtle is winner!")


screen.exitonclick()
