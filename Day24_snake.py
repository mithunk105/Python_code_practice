from turtle import Turtle
START_POSITIONS = [(0, 0), (-5, 0), (-10, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.all_segment = []
        self.create_snake()
        self.head = self.all_segment[0]

    def add_snake(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.all_segment.append(snake)

    def create_snake(self):
        for pos in START_POSITIONS:
            self.add_snake(pos)

    def extend_snake(self):
        self.add_snake(self.all_segment[-1].position())

    def move(self):
        for i in range(len(self.all_segment) - 1, 0, -1):
            newx = self.all_segment[i - 1].xcor()
            newy = self.all_segment[i - 1].ycor()
            self.all_segment[i].goto(newx, newy)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.all_segment:
            segment.goto(2000, 2000)
        self.all_segment.clear()
        self.create_snake()
        self.head = self.all_segment[0]