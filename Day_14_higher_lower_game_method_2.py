import random


def game_logo():
    print("="*138)
    print("="*59, "Higher lower game", "="*59)
    print("="*138)
#____________________________________________________________________________________________________

def hl_game():
    demography = [
        ("Tokyo", 37.4), ("Delhi", 31.0), ("Shanghai", 27.1), ("Sao Paulo", 22.0),
        ("Mexico City", 21.8), ("Cairo", 20.9), ("Dhaka", 20.3), ("Mumbai", 20.2),
        ("Beijing", 20.0), ("Osaka", 19.1), ("Karachi", 16.1), ("Chongqing", 15.9),
        ("Istanbul", 15.8), ("Buenos Aires", 15.2), ("Kolkata", 14.9),
        ("Lagos", 14.8), ("Kinshasa", 14.3), ("Manila", 14.0),
        ("Tianjin", 13.9), ("Guangzhou", 13.5), ("Rio de Janeiro", 13.0),
        ("Lahore", 12.6), ("Bangalore", 12.3), ("Paris", 11.1),
        ("Bogota", 11.0), ("Jakarta", 10.8), ("Chennai", 10.7),
        ("Lima", 10.7), ("Bangkok", 10.5), ("Seoul", 9.9),
        ("Nagoya", 9.6), ("Hyderabad", 9.4), ("London", 9.0),
        ("Tehran", 8.7), ("Chicago", 8.6), ("Chengdu", 8.3),
        ("Nanjing", 8.2), ("Wuhan", 8.1), ("Ho Chi Minh City", 8.0),
        ("Luanda", 7.9), ("Ahmedabad", 7.8), ("Kuala Lumpur", 7.7),
        ("Xi'an", 7.5), ("Hong Kong", 7.4), ("Dongguan", 7.3),
        ("Hangzhou", 7.2), ("Foshan", 7.1), ("Shenyang", 7.0),
        ("Riyadh", 6.9), ("Baghdad", 6.8)
    ]

    random.shuffle(demography)
    tot_cities = len(demography)
    ran_num_1 = random.randint(0, tot_cities-1)
    score = 0
    while True:
        tot_cities = len(demography)
        if tot_cities < 2:
            print("No more cities left. You won!")
            break
        else:
            ran_num_2 = random.choice([x for x in range(tot_cities) if x != ran_num_1])
            user_input = input(f"\nWhich city has higher population?\na: '{demography[ran_num_1][0]}' | b: '{demography[ran_num_2][0]}' : ").lower()

            if user_input == "a":
                if demography[ran_num_1][1] > demography[ran_num_2][1]:
                    demography.pop(ran_num_2)
                    ran_num_1 = ran_num_1 - 1 if ran_num_2 <= ran_num_1 else ran_num_1
                    print("You are correct.")
                    score += 1
                    print("Score: ", score)
                elif demography[ran_num_1][1] < demography[ran_num_2][1]:
                    print("You are wrong.")
                    print("Score: ", score)
                    break
                else:
                    print("Oops! These cities have similar population. Skipping to next city.")
            elif user_input == "b":
                if demography[ran_num_1][1] > demography[ran_num_2][1]:
                    print("You are wrong.")
                    print("Score: ", score)
                    break
                elif demography[ran_num_1][1] < demography[ran_num_2][1]:
                    demography.pop(ran_num_1)
                    ran_num_1 = ran_num_2 if ran_num_2 <= ran_num_1 else ran_num_2 - 1
                    print("You are correct.")
                    score += 1
                    print("Score: ", score)
                else:
                    print("Oops! These cities have similar population. Skipping to next city.")
            else:
                print("Please enter a valid input.")

def final_hl_game():
    game_logo()
    hl_game()
    while True:
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again == "y":
            print("\n"*10)
            game_logo()
            hl_game()
        elif play_again == "n":
            print("\nThank you for playing.")
            break
        else:
            print("Please enter a valid input(y/n).")

final_hl_game()