from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=6, stretch_wid=1)
        self.setheading(90)
        self.goto(x, y)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)