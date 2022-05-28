import turtle as t

turtle = t.Turtle()
screen = t.Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def counter_clockwise():
    turtle.left(10)


def clockwise():
    turtle.right(10)


def clear_screen():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
