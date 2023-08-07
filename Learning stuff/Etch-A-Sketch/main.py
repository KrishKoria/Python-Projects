from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_backwards():
    tim.backward(10)


def move_forwards():
    tim.forward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.pu()
    tim.clear()
    tim.home()
    tim.pd()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
