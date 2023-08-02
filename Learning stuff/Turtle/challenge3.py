import random
from turtle import Turtle

tim = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


def draw_shape(num):
    angle = 360 / num
    for _ in range(num):
        tim.forward(100)
        tim.rt(angle)


for n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(n)
