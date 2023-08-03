import random
import turtle as t


def draw_dot():
    tim.dot(20, random.choice(colors_list))
    tim.fd(100)


def set_direction():
    tim.setheading(90)
    tim.fd(75)
    tim.setheading(180)
    tim.fd(1000)
    tim.setheading(0)


def draw(times):
    for dots in range(1, times + 1):
        draw_dot()
        if dots % 10 == 0:
            set_direction()


colors_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
               (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
               (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
               (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
               (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.pu()
tim.goto(-700, -300)
tim.speed("fastest")

draw(100)

screen = t.Screen()
screen.exitonclick()
screen.setup(300, 300)
