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
                   
Type "quit" to exit the game.
""")


import random


animals = ['Tiger', "Elephant", "Horse", "Moose"]

chosen_word = random.choice(animals).lower()
word_to_guess_list = ["_"]*len(chosen_word)


lives = 5
already_guessed = set()

game_over = False

while not game_over:
    print("\nWord to guess : ", " ".join(word_to_guess_list))
    if already_guessed:
        print("Already guessed letter (or letters) : ", ", ".join(sorted(already_guessed)))
    guess = input("Guess a letter: ").lower()

    if guess == "quit":
        print("You left the game.")
        game_over = True
    else:

        if len(guess) == 0:
            print(f"Please enter at least one letter. \nlives left :", lives)
        elif len(guess) > 1:
            print(f"Multi-letter guessing is not allowed. \nlives left :", lives)
        elif not guess.isalpha():
            print(f"{guess} is not a letter. Please try again. \nlives left :", lives)

        elif len(guess) == 1:
            if guess in already_guessed:
                print(f"You already guessed this letter. Please try again. \nlives left :", lives)
            else:
                for i, l in enumerate(chosen_word):
                    if l == guess:
                        word_to_guess_list[i] = guess


                if guess in chosen_word:
                    print("Your guess is correct.\nWord after guessing correct letter : ", " ".join(word_to_guess_list))
                    print("lives left :", lives)
                else:
                    lives -= 1
                    if lives != 0:
                        print("Your guess is incorrect. You have lost one life. \nlives left :", lives)

                already_guessed.add(guess)

                if "_" not in word_to_guess_list:
                    print("\nYaY! You guessed it correctly. You won 🏆")
                    game_over = True
                elif lives == 0:
                    print("\nOh no! Your guess is incorrect. You lost 😞\nThe correct word is ", chosen_word)
                    game_over = True