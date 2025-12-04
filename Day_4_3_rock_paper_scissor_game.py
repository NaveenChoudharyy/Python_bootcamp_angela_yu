# Rock Paper Scissors Game

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

game_img = [rock_img, paper_img, scissor_img]


your_choice = input("Choose rock, paper or scissor: ").lower()
choose_one = ["rock", "paper", "scissor"]
computer_choice = random.choice(choose_one)

if your_choice in choose_one:

    # when your_choice = rock and computer_choice = paper

    if your_choice == "rock" and computer_choice == "paper":
        print("your choice : rock")
        print(game_img[game_img.index(rock_img)])
        print("computer's choice : paper")
        print(game_img[game_img.index(paper_img)])
        print("You loose!")

    # when your_choice = rock and computer_choice = scissor
    elif your_choice == "rock" and computer_choice == "scissor":
        print("your choice : rock")
        print(game_img[game_img.index(rock_img)])
        print("computer's choice : scissor")
        print(game_img[game_img.index(scissor_img)])
        print("You wins!")

    # when your_choice = paper and computer_choice = rock
    elif your_choice == "paper" and computer_choice == "rock":
        print("your choice : paper")
        print(game_img[game_img.index(paper_img)])
        print("computer's choice : rock")
        print(game_img[game_img.index(rock_img)])
        print("You wins!")

    # when your_choice = paper and computer_choice = scissor
    elif your_choice == "paper" and computer_choice == "scissor":
        print("your choice : paper")
        print(game_img[game_img.index(paper_img)])
        print("computer's choice : scissor")
        print(game_img[game_img.index(scissor_img)])
        print("You loose!")

    # when your_choice = scissor and computer_choice = rock
    elif your_choice == "scissor" and computer_choice == "rock":
        print("your choice : scissor")
        print(game_img[game_img.index(scissor_img)])
        print("computer's choice : rock")
        print(game_img[game_img.index(rock_img)])
        print("You loose!")

    # when your_choice = scissor and computer_choice = paper
    elif your_choice == "scissor" and computer_choice == "paper":
        print("your choice : scissor")
        print(game_img[game_img.index(scissor_img)])
        print("computer's choice : paper")
        print(game_img[game_img.index(paper_img)])
        print("You wins!")

    # when your_choice = rock and computer_choice = rock
    elif your_choice == "rock" and computer_choice == "rock":
        print("your choice : rock")
        print(game_img[game_img.index(rock_img)])
        print("computer's choice : rock")
        print(game_img[game_img.index(rock_img)])
        print("Tie-breaker!")

    # when your_choice = paper and computer_choice = paper
    elif your_choice == "paper" and computer_choice == "paper":
        print("your choice : paper")
        print(game_img[game_img.index(paper_img)])
        print("computer's choice : paper")
        print(game_img[game_img.index(paper_img)])
        print("Tie-breaker!")

    # when your_choice = scissor and computer_choice = scissor
    elif your_choice == "scissor" and computer_choice == "scissor":
        print("your choice : scissor")
        print(game_img[game_img.index(scissor_img)])
        print("computer's choice : scissor")
        print(game_img[game_img.index(scissor_img)])
        print("Tie-breaker!")

else:
    print("Please enter a valid input. Try again.")
