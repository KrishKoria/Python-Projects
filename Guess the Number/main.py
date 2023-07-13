import random as rd
from art import logo

print(logo)
EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def game(lives, comp_value) :
    comp_guess = comp_value
    # print(comp_guess)
    while lives != 0 :
        print(f"You have {lives} attempts remaining to guess a number")
        guess = int(input("Make a guess: "))
        if comp_guess < guess :
            print("Too High")
            print("Guess Again")
        elif comp_guess > guess :
            print("Too Low")
            print("Guess Again")
        elif comp_guess == guess :
            print(f"You Got it!!, Answer was {comp_guess}")
            return
        lives -= 1


print("Welcome to Guess The Number!!!")
print("I am thinking of a number between 1 and 100")
choice = input("Choose Your Difficulty, Easy or Hard: ").lower()
value = rd.randint(1, 100)
if choice == 'easy' :
    game(EASY_LEVEL_LIVES, value)
elif choice == 'hard' :
    game(HARD_LEVEL_LIVES, value)
else :
    print("You have entered wrong option!!!")
