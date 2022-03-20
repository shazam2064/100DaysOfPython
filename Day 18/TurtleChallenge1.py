######## Challenge 1 - Draw a Square ############
from turtle import Turtle
import turtle as t

timmy_the_turtle = t.Turtle()

for _ in range(4):
    timmy_the_turtle.shape("turtle")
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

