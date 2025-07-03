import random
from Hangman_game_words import word_list
from Hangman_game_images import logo, stages


lives = 6
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder =""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"**********{lives}/6 Lives Left.**********")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display =""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display +="_"

    print("word to guess: " +display)



    if guess not in chosen_word:
        lives -=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"********** It was {chosen_word}.You Lose.**********")

    if "_" not in display:
        game_over = True
        print("**********You Win.**********")

    print(stages[lives])