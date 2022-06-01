from turtle import Screen
from crossing_turtle import CTurtle
from cars_on_road import RCars
from screen_display import Display
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cturtle = CTurtle()
rcar = RCars()
display = Display()
screen.listen()
screen.onkey(fun=cturtle.move, key="Up")
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(.1)

    rcar.create_cars()
    rcar.move_cars()

    for car in rcar.car_list:
        if car.distance(cturtle) < 20:
            is_game_on = False
            display.game_over()

    if cturtle.ycor() >= 280:
        display.update_level()
        rcar.increase_speed()
        cturtle.reset()


screen.exitonclick()
