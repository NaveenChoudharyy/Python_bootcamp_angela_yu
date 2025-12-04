import random

rock_img = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_img = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor_img = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# The order of these two lists MUST match!
choose_one = ["rock", "paper", "scissor"]
game_img = [rock_img, paper_img, scissor_img]

# --- Game Logic ---

your_choice = input("Choose rock, paper or scissor: ").lower()

if your_choice in choose_one:

    # 1. Get the indices for easy reference
    your_index = choose_one.index(your_choice)
    computer_index = random.randint(0, 2)
    computer_choice = choose_one[computer_index]

    # 2. Print both choices and images ONCE
    print(f"\nYour choice: {your_choice}")
    print(game_img[your_index])
    print(f"Computer's choice: {computer_choice}")
    print(game_img[computer_index])

    # 3. Check for the result using the simplified logic

    if your_index == computer_index:
        # Tie condition
        print("Tie-breaker!")
    elif (your_index == 0 and computer_index == 2) or \
            (your_index == 1 and computer_index == 0) or \
            (your_index == 2 and computer_index == 1):
        # Winning conditions: (Rock=0 beats Scissor=2) OR (Paper=1 beats Rock=0) OR (Scissor=2 beats Paper=1)
        print("You win! 🎉")
    else:
        # Losing condition (covers all remaining cases)
        print("You lose! 😢")

else:
    print("Please enter a valid input. Try again.")