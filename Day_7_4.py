import random

fruits = ["apple", "banana", "apricot"]

computer_chosen_word = random.choice(fruits).lower()

guessed_word = ["_"] * len(computer_chosen_word)
word_to_guess = " ".join(guessed_word)
print("Word to guess : ", word_to_guess)

tries_left = 5
already_guessed = []

while (tries_left > 0) and ("_" in guessed_word):
    print("")
    your_guess = input("Guess the word and press enter : ")

    if len(your_guess) == 1:
        your_guess = your_guess.lower()

        # LOGIC FIX 1: Check duplicates FIRST, before processing the word
        if your_guess in already_guessed:
            print(f"You already guessed '{your_guess}'. Try with different letter.")
            print(f"You have {tries_left} tries left.")

        # If it is a NEW guess
        else:
            already_guessed.append(your_guess)

            if your_guess in computer_chosen_word:
                # Update the blanks
                for i, letter in enumerate(computer_chosen_word):
                    if letter == your_guess:
                        guessed_word[i] = letter
                print(f"Correct! You have {tries_left} tries left.")
            else:
                tries_left -= 1
                print(f"Your guess is incorrect. You have {tries_left} tries left.")

    elif len(your_guess) == 0:
        print("Please enter at least a letter.")
    else:
        print("More than one letter is not allowed. Try again.")

    # LOGIC FIX 2: Print the board at the END of the loop
    # This ensures the user sees the word even if they made a mistake/duplicate guess
    print(" ".join(guessed_word))

if "_" in guessed_word:
    print(f"\nYou lost 😞. The correct word was '{computer_chosen_word}'.")
else:
    print(f"\nYaY! You won 🏆. You guessed it correctly. The correct word is '{computer_chosen_word}'.")