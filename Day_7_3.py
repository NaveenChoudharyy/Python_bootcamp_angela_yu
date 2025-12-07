import random

fruits = ["apple","banana","Orange"]
computer_chosen_word = random.choice( fruits).lower()


Guess_word = ["_"] * len(computer_chosen_word)
print("Word to be guessed : ",Guess_word)


guess_times = 0
total_guesses = 10
while total_guesses > guess_times:
    print("")
    guess_input = input("Guess the word : ").lower()
    if guess_input  in computer_chosen_word:
        for i, letter in enumerate(computer_chosen_word):
            if guess_input == letter:
                Guess_word[i] = letter
    else:
        guess_times += 1
        print("Your input is incorrect. You lost 1 life.")
    Guess_remains = total_guesses - guess_times
    print("".join(Guess_word))
    print(f"Guess remains : {Guess_remains}")


if "_" in Guess_word:
    print("")
    print("You lost😞")
else:
    Guessed_word = "".join(Guess_word)
    print("")
    print("Guessed word : ", Guessed_word)
    print("You won🏆")