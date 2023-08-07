from turtle import Turtle, Screen

tim = Turtle()
tim.pu()
screen = Screen()
bet = screen.textinput(title="Make Your Bet", prompt="Which Turtle will win the Race? Enter A color :- ")
print(bet)
tim.goto(-750, -350)

screen.exitonclick()
