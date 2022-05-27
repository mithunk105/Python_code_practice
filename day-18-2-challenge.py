import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
screen = t.Screen()

tim.shape("arrow")
tim.forward(10)

for _ in range(10):
  tim.penup()
  tim.forward(10)
  tim.pendown()
  tim.forward(10)

screen.exitonclick()