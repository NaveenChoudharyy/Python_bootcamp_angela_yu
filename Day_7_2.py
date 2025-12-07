import random

fruits = ["apple","banana","Orange"]

comp_chosen_word = random.choice(fruits).lower()

Guess_word = ""
for _ in range(0,len(comp_chosen_word)):
    Guess_word += "_"
print("Word to be guessed : ", Guess_word)

guess = input("Guess a word? : ").lower()

display = ""
for i, letter in enumerate(comp_chosen_word):
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)

"""

# Created by me 
# It will take longer to run this code so not using this

for i, letter in enumerate(comp_chosen_word):
    Guess_word = list(Guess_word)
    if letter == guess:
        Guess_word[i] = letter
    Guess_word = "".join(Guess_word)
print("Guess word : ", Guess_word)
"""