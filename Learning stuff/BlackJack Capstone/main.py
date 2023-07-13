import random as rd
from art import logo


def deal_cards() :
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = rd.choice(cards)
    return card


def calculate_score(cards) :
    if sum(cards) == 21 and len(cards) == 2 :
        return 0
    elif sum(cards) > 21 and 11 in cards :
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, comp_score) :
    if user_score > 21 and comp_score > 21 :
        print("You went over, You lose :( ")
    elif user_score > 21 :
        print("You went over, You lose :( ")
    elif user_score == 0 :
        print("You WON!!,you had blackjack")
    elif comp_score == 0 :
        print("You Lost!! as computer had Blackjack")
    elif user_score > comp_score :
        print("You Won :) ")
    elif comp_score > 21 :
        print("Opponent went over, You Win :) ")
    else :
        print("You Lose :( ")


def blackjack() :
    comp_score = 0
    user_score = 0
    print(logo)
    cards_user = []
    cards_comp = []
    game_over = False
    for i in range(2) :
        cards_user.append((deal_cards()))
        cards_comp.append((deal_cards()))
    while not game_over :
        user_score = calculate_score(cards_user)
        comp_score = calculate_score(cards_comp)
        print(f"Your Hand: {cards_user}      Your Score: {user_score}")
        print(f"Computer's First card: {cards_comp[0]}")
        if user_score != 0 and comp_score != 0 and user_score <= 21 :
            should_deal = input("Type y for another card,type n to pass :- ").lower()
            if should_deal == 'y' :
                cards_user.append((deal_cards()))
            else :
                game_over = True
        else :
            game_over = True
    while comp_score < 17 and comp_score != 0 :
        cards_comp.append(deal_cards())
        comp_score = calculate_score(cards_comp)
    print(f"Your Final Hand: {cards_user}      Your Score: {user_score}")
    print(f"Computer's Final Hand: {cards_comp}   Computer Score: {comp_score}")
    compare(user_score, comp_score)


choice = input("Do you want to play BlackJack, y for yes or n for no :- ").lower()
if choice == 'y' :
    blackjack()
else :
    print("thank you for using blackjack program")
