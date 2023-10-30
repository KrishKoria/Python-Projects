from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as file:
            self.highScore = int(file.read())
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 400)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highScore}", align="center", font=("Ariel", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_board()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER !!", align="center", font=("Ariel", 30, "normal"))
    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
        with open("data.txt", "w") as file:
            file.write(f"{self.highScore}")
        self.score = 0
        self.update_board()
