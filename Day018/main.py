import turtle
import colorgram
import random
from turtle import Turtle, Screen
import turtle as t
t.colormode (255)
turtle.colormode()

# TODO: generating color list
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [
              (236, 35, 108), (145, 28, 66), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47),
              (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56),
              (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193), (145, 27, 25),
              (243, 167, 156), (163, 211, 178), (26, 187, 225), (6, 116, 54), (138, 210, 232), (74, 135, 184),
              (170, 191, 221), (114, 10, 8)
            ]

timmy = Turtle()
timmy.hideturtle()
timmy.speed(2)
turtle.colormode()

def paint():
    timmy.penup()
    timmy.setheading(225)
    timmy.forward(343.55)
    for _ in range(10):
        for _ in range(10):
            timmy.setheading(0)
            timmy.dot(20,random.choice(color_list))
            timmy.forward(50)
        timmy.setheading(174.29)
        timmy.forward(502.5)
paint()

screen = Screen()
screen.exitonclick()
