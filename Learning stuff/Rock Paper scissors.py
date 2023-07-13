import random as rd

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
choice = int(input("Enter 0 for rock,1 for paper or 2 for scissors :- "))
if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[choice])
comp_choice = rd.randint(0,2)
print(f"Computer Chose {comp_choice}")
print(game_images[comp_choice])

if choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice == 0 and choice == 2:
    print("You lose")
elif comp_choice > choice:
    print("You lose")
elif choice > comp_choice:
    print("You win!")
elif comp_choice == choice:
    print("It's a draw")
