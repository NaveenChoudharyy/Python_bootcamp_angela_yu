import random

#____________________________________________________________________________________________________

def game_print():
    print("="*138)
    print("="*56, "Guess the number game", "="*56)
    print("="*138)

#____________________________________________________________________________________________________

def game_start():
    computer_guess = random.randint(1,100)
    return computer_guess

#____________________________________________________________________________________________________

def select_level():
    attempts = 0
    while True:
        easy_or_hard = input("\nplease select the level (easy/hard): ").lower()
        if easy_or_hard in ["easy", "hard"]:
            break
        else:
            print("You can only select levels as easy or hard.")

    if easy_or_hard == "easy":
        attempts += 10
        print(f"You got {attempts} attempts.")
    elif easy_or_hard == "hard":
        attempts += 5
        print(f"You got {attempts} attempts.")
    return easy_or_hard, attempts

#____________________________________________________________________________________________________

def let_user_guess():
    while True:
        try:
            user_guess = int(input("\nGuess a number from 1 to 100: "))
            return user_guess
        except ValueError:
            print("You can only enter a number between 1 and 100 including both endpoints.")

#____________________________________________________________________________________________________

def user_num_check():
    user_guess = let_user_guess()
    while True:
        if 100 >= user_guess >= 1:
            break
        else:
            print("You can only enter a number between 1 and 100 including both endpoints.")
            user_guess = let_user_guess()
    return user_guess

#____________________________________________________________________________________________________

def compare():
    computer_guess = game_start()
    easy_or_hard, attempts = select_level()
    tot_attempts = attempts
    user_guess = user_num_check()
    while attempts > 0:
        if user_guess == computer_guess:
            attempts -= 1
            print(f"You guessed the correct number! You took {tot_attempts - attempts} attempts to guess the correct number.")
            break

        elif user_guess < computer_guess:
            attempts -= 1
            print("Your guess is too low!")
            print("Attempts left: ", attempts)
            if attempts > 0:
                user_guess = user_num_check()
            else:
                print(f"You've run out of attempts! The correct number was {computer_guess}.")

        elif user_guess > computer_guess:
            attempts -= 1
            print("Your guess is too high.")
            print("Attempts left: ", attempts)
            if attempts > 0:
                user_guess = user_num_check()
            else:
                print(f"You've run out of attempts! The correct number was {computer_guess}.")

#____________________________________________________________________________________________________

def play_again_ask():
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "no"]:
            break
        else:
            print("You can only select 'yes' or 'no'.")
    return play_again

#____________________________________________________________________________________________________

def final_game():
    game_print()
    compare()
    play_again = play_again_ask()
    return play_again

#____________________________________________________________________________________________________

def guess_the_number_game():
    play_again = final_game()
    while True:
        if play_again == "yes":
            print("\n"*20)
            play_again = final_game()
        else:
            print("\nThank you for playing!.")
            break

#------------------------------------------>Code ends here<------------------------------------------