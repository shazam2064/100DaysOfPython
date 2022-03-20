from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

TURTLE_SIZE = 20
screen = Screen()

tim = Turtle(shape="turtle", visible=False)
tim.penup()
tim.goto(TURTLE_SIZE / 2 - screen.window_width() / 2, screen.window_height() / 2 - TURTLE_SIZE / 2)
tim.pendown()
tim.showturtle()
tim.speed("fastest")


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 1000):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

