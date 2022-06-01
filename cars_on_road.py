from turtle import Turtle
from random import randint, choice
COLOURS = ["red", "blue", "yellow", "violet", "indigo", "green", "orange"]
NEG_Y_DIR = -240
POS_Y_DIR = 260


class RCars:

    def __init__(self):
        self.car_list = []
        self.car_speed = 5
        self.create_cars()

    def create_cars(self):
        rand = randint(1, 6)
        if rand == 1:
            car = Turtle()
            car.shape("square")
            car.color(choice(COLOURS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(300, randint(NEG_Y_DIR, POS_Y_DIR))
            self.car_list.append(car)

    def move_cars(self):
        for i in range(len(self.car_list)):
            self.car_list[i].backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 10
