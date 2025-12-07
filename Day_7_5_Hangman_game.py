# Hangman Game

import random

animals = ['Tiger', "Elephant", "Horse"]

chosen_word = random.choice(animals).lower()
word_to_guess_list = ["_"]*len(chosen_word)


lives = 3
already_guessed = []

game_over = False

while not game_over:
    print("")
    guess = input("Guess a letter: ").lower()
    print("".join(word_to_guess_list))

    if len(guess) == 1:
        if guess not in already_guessed:

            for i, letter in enumerate(chosen_word):
                if  guess == letter:
                    word_to_guess_list[i] = letter
                    word_to_guess = "".join(word_to_guess_list)

                    print(f"word_to_guess_list : {word_to_guess}")

                elif letter not in chosen_word:
                    lives -= 1
                    print(f"Incorrect guess. You have lost 1 live here. Now you have {lives}/3 lives.")

                if lives == 0 and "_" in word_to_guess_list:
                    game_over = True
                    print(f"Your guess is incorrect. You have lost all your lives. The correct word is {chosen_word}.")

            already_guessed.append(guess)

        else:
            print(f"You already guessed this word. Please try again. You still have {lives}/3 lives left.")

    elif len(guess) == 0:
        print(f"Please enter at least one letter. You still have {lives}/3 lives left.")
    else:
        print(f"Multi-letter guessing is not allowed. You still have {lives}/3 lives left.")

