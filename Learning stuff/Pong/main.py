from turtle import Turtle, Screen
from Paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
ball = Ball()
left = Paddle(350, 0)
right = Paddle(-350, 0)
screen.listen()

screen.onkeypress(left.go_up, 'Up')
screen.onkeypress(left.go_down, 'Down')

screen.onkeypress(right.go_up, 'w')
screen.onkeypress(right.go_down, 's')

game_on = True
while game_on:
    screen.update()
screen.exitonclick()
