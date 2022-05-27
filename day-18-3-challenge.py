import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shape(sides):
  angle = 360/sides
  for _ in range(sides):
    tim.forward(100)
    tim.right(angle)

tim.shape("arrow")
for shape_num in range(3, 11):
  tim.color(random.choice(colours))
  draw_shape(shape_num)