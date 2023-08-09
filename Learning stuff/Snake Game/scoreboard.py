from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 400)
        self.update_board()

    def update_board(self):
        self.write(f"Score : {self.score}", align="center", font=("Ariel", 24, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER !!", align="center", font=("Ariel", 30, "normal"))
