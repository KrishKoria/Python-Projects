import random as rd
from art import logo, vs
from game_data import data

score = 0
game_over = False
B = rd.choice(data)


def game(choiceA, choiceB) :
    print(f"Compare A: {choiceA['name']}, {choiceA['description']}, {choiceA['country']}")
    print(vs)
    print(f"Compare B: {choiceB['name']}, {choiceB['description']}, {choiceB['country']}")
    choice = input("Who has More Followers? Type A or B: ").lower()
    if choice == 'a' and choiceA['follower_count'] > choiceB['follower_count'] :
        return 1
    elif choice == 'b' and choiceB['follower_count'] > choiceA['follower_count'] :
        return 1
    else :
        return 0


while not game_over :
    print(logo)
    A = B
    B = rd.choice(data)
    if A == B :
        B = rd.choice(data)
    c = game(A, B)
    if c == 1 :
        score += 1
        print(f"You are Correct!!! Score is {score}")
    elif c == 0 :
        print(f"Sorry,That's the wrong answer,Score is {score}")
        game_over = True
