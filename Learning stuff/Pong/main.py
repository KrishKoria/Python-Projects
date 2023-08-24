from turtle import Turtle, Screen
from Paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
ball = Ball()
right = Paddle(350, 0)
left = Paddle(-350, 0)
screen.listen()
score_board = Scoreboard()
screen.onkeypress(right.go_up, 'Up')
screen.onkeypress(right.go_down, 'Down')

screen.onkeypress(left.go_up, 'w')
screen.onkeypress(left.go_down, 's')

game_on = True
while game_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_upper_wall()
    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()
screen.exitonclick()
