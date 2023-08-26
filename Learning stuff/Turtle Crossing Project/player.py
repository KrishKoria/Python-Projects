from turtle import Turtle

STARTING_POSITION = (0, -380)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 380


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.go_starting()
        self.setheading(90)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def is_finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_starting(self):
        self.goto(STARTING_POSITION)
