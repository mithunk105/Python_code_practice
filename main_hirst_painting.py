# import colorgram as cg
# color = cg.extract("image.jpg", 40)
# color_list = []
# for i in range(0, len(color)):
#     r = color[i].rgb.r
#     g = color[i].rgb.g
#     b = color[i].rgb.b
#     color_list.append((r, g, b))
# print(color_list) --> list extracted from hirst image to create hirst painting using python
import turtle as t
import random
t.colormode(255)
color_list = [(199, 174, 117), (125, 37, 24), (163, 103, 56), (184, 158, 53), (6, 56, 82), (108, 68, 85), (46, 34, 32), (113, 160, 175), (23, 121, 170), (75, 37, 47), (66, 153, 135), (9, 66, 46), (87, 139, 59), (130, 39, 42), (182, 96, 80), (204, 202, 144), (144, 175, 158), (171, 151, 156), (178, 201, 185), (221, 181, 167), (31, 78, 61), (24, 76, 91), (88, 142, 156), (161, 108, 112), (213, 179, 182), (169, 199, 209), (37, 66, 94), (94, 131, 165), (180, 191, 207), (65, 64, 62)]
tim = t.Turtle()
screen = t.Screen()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dots in range(1, 101):
    tim.dot(15, random.choice(color_list))
    tim.forward(50)

    if dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()
