import random

fruits = ["apple","banana","Orange"]

chosen_word = random.choice(fruits).lower()
guess = input("Guess a word? : ").lower()

print("")

for letter in chosen_word:
    if letter == guess:
        print(letter)
    else:
        print("_")

print("")
print("Chosen word : ",chosen_word)


