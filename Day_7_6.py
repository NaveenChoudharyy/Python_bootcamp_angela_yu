# Hangman Game

print(r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                        
""")

import random

animals = ['Tiger', "Elephant", "Horse"]

chosen_word = random.choice(animals).lower()
word_to_guess_list = ["_"] * len(chosen_word)

lives = 3
already_guessed = set()   # use a set for O(1) membership checks

game_over = False

while not game_over:
    print()
    print("Word to guess : ", " ".join(word_to_guess_list))
    if already_guessed:
        print("Already guessed:", " ".join(sorted(already_guessed)))
    guess = input("Guess a letter: ").lower()

    # basic validation
    if len(guess) == 0:
        print(f"Please enter at least one letter. \nlives left : {lives}")
        continue
    if len(guess) > 1:
        print(f"Multi-letter guessing is not allowed. \nlives left : {lives}")
        continue
    if not guess.isalpha():
        print(f"Please enter a letter (a-z). \nlives left : {lives}")
        continue

    if guess in already_guessed:
        print(f"You already guessed this letter. Please try again. \nlives left : {lives}")
        continue

    # mark guessed (so repeating same guess later is handled)
    already_guessed.add(guess)

    # reveal matches
    for i, l in enumerate(chosen_word):
        if l == guess:
            word_to_guess_list[i] = guess

    if guess in chosen_word:
        print("Your guess is correct.")
        print("Word after guessing correct letter : ", " ".join(word_to_guess_list), f"\nlives left : {lives}")
    else:
        lives -= 1
        if lives > 0:
            print("Your guess is incorrect. You have lost one life. \nlives left :", lives)
        else:
            # no lives left
            print("\nOh no! Your guess is incorrect. You lost😞")
            game_over = True
            break

    # win check
    if "_" not in word_to_guess_list:
        print("\nYaY! You guessed it correctly. You won 🏆")
        game_over = True
