import random


def game_logo():
    print("="*138)
    print("="*59, "Higher lower game", "="*59)
    print("="*138)

#____________________________________________________________________________________________________

def demo():
    """Returns demography dict which contains list of cities and their populations."""
    cities = ["Dongguan", "Paris", "Ahmedabad", "Lima", "Tokyo", "Foshan", "Chicago", "Baghdad", "Hyderabad",
              "Osaka", "Nagoya", "Delhi", "Kuala Lumpur", "Bangkok", "Tianjin", "London", "Wuhan",
              "Rio de Janeiro", "Beijing", "Riyadh", "Bangalore", "Tehran", "Chennai", "Karachi", "Manila",
              "Shanghai", "Bogota", "Seoul", "Chongqing", "Jakarta", "Hong Kong", "Guangzhou", "Lagos",
              "Ho Chi Minh City", "Kinshasa", "Nanjing", "Sao Paulo", "Istanbul", "Mumbai", "Shenyang",
              "Xi'an", "Kolkata", "Luanda", "Hangzhou", "Mexico City", "Buenos Aires", "Cairo", "Dhaka",
              "Lahore", "Chengdu"]
    populations = [ 7.3, 11.1, 7.8, 10.7, 37.4, 7.1, 8.6, 6.8, 9.4, 19.1, 9.6, 31.0, 7.7, 10.5, 13.9,
                    9.0, 8.1, 13.0, 20.0, 6.9, 12.3, 8.7, 10.8, 16.1, 14.0, 27.1, 11.0, 9.9, 15.9, 10.8,
                    7.4, 13.5, 14.8, 8.0, 14.3, 8.2, 22.0, 15.8, 20.2, 7.0, 7.5, 14.9, 7.9, 7.2, 21.8,
                    15.2, 20.9, 20.3, 12.6, 8.3 ]
    demography = {"city":cities, "population": populations}

    return demography

#____________________________________________________________________________________________________

def user_choice(ran_num_1, demography):
    ran_num_2 = random.choice([x for x in range(0, len(demography['city'])) if x != ran_num_1])

    while True:
        user_input = input(
            f"\nWhich city has higher population? (A/B): \nCity A: {demography['city'][ran_num_1]} |City B: {demography['city'][ran_num_2]}\n").lower()
        if user_input == "a" or user_input == "b":
            break
        else:
            print("Please enter a valid input. You can type only 'A' or 'B'. Try again.")

    return user_input, ran_num_2

#____________________________________________________________________________________________________

def game(demography):
    game_logo()
    score = 0
    ran_num_1 = random.randint(0, len(demography['city'])-1)
    while True:
        user_input, ran_num_2 = user_choice(ran_num_1, demography)

        if user_input == "a" and demography["population"][ran_num_1] > demography["population"][ran_num_2]:
            score += 1
            print(f"You are correct! Lets move to next round.")
            print("Your score is: ", score)
            if demography["city"][ran_num_1] == 'Tokyo':
                while True:
                    if  demography["city"][ran_num_1] == 'Tokyo':
                        ran_num_1 = random.randint(0, len(demography['city'])-1)
                    else:
                        break
        elif user_input == "a" and demography["population"][ran_num_1] < demography["population"][ran_num_2]:
            print(f"You are wrong!")
            print("Your score is: ", score)
            break
        elif user_input == "b" and demography["population"][ran_num_1] > demography["population"][ran_num_2]:
            print(f"You are wrong!")
            print("Your score is: ", score)
            break
        elif user_input == "b" and demography["population"][ran_num_1] < demography["population"][ran_num_2]:
            score += 1
            print(f"You are correct! Lets move to next round.")
            print("Your score is: ", score)
            ran_num_1 = ran_num_2
            if demography["city"][ran_num_1] == 'Tokyo':
                while True:
                    if  demography["city"][ran_num_1] == 'Tokyo':
                        ran_num_1 = random.randint(0, len(demography['city'])-1)
                    else:
                        break

#____________________________________________________________________________________________________

def play_higher_lower():
    demography = demo()
    game(demography)
    while True:
        play_again = input(f"\nDo you want to play again? (y/n) : ").lower()
        if play_again == "y":
            print("\n"*20)
            game(demography)
        elif play_again == "n":
            print(f"\nThank you for playing!")
            break
        else:
            print("Please select the correct option. Try again.")

play_higher_lower()