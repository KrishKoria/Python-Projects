from turtle import Turtle, Screen

tim = Turtle()
for _ in range(25):
    tim.fd(5)
    tim.pu()
    tim.fd(5)
    tim.pd()
screen = Screen()
screen.exitonclick()
