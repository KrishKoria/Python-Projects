import random as rd
import hangman_words as hw
import hangman_art as ha

chosen_word = rd.choice(hw.word_list)
word_length = len(chosen_word)
display = []
lives = 6
end_of_game = False
for n in range(0, word_length):
    display += '_'
print(ha.logo)
print(f'Pssst, the solution is {chosen_word}.')
while not end_of_game:
    guess = input("Guess a Letter :- ").lower()
    if guess in display:
        print(f"{guess} is already in the letter,Try another letter")

    for position in range(0, word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print("You Won !!!")

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word,Try again")
        if lives == 0:
            end_of_game = True
            print("You Lose !!!")

    print(ha.stages[lives])
