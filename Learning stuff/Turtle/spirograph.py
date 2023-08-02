import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tim.color(color)
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
