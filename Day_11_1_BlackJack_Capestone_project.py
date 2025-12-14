import random


BlackJack_game_logo =r'''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ )||          | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  / ||          | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ A||          | |_) | | (_| | (__|   <| | (_| | (__|   < 
`------'|          |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
 `------'                                 _/ |                
                                         |__/
'''

deck = []

def reset_deck():
    global deck
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4
    random.shuffle(deck)



def deal_card():
    global deck
    if len(deck) == 0:
        reset_deck()
    index = deck.index(random.choice(deck))
    card = deck.pop(index)
    return card



# Distributing first 2 cards
def first_2_cards():
    user = []
    comp = []

    for a in range(2):
        user.append(deal_card())

    for b in range(2):
        comp.append(deal_card())

    print("User's cards : ",user)
    print("Comp's cards : ",[comp[0]]+["*"])

    return user, comp


# Condition checking if any of the player already won or match drew after drawing first 2 cards.
def first_2_cards_check(user, comp):

    game_end = 1

    if sum(user) > 21 and user.count(11) > 0:
        user[user.index(11)] = 1

    if sum(comp) > 21 and comp.count(11) > 0:
        comp[comp.index(11)] = 1

    if sum(user) == 21 and sum(comp) == 21:
        print("\nUser's cards : ", user, "| Sum ; ", sum(user))
        print("Comp's cards : ", comp, "| Sum ; ", sum(comp))
        print("Game draw!")
        game_end = 0

    elif sum(user) == 21:
        print("\nUser's cards : ", user, "| Sum ; ", sum(user))
        print("Comp's cards : ", comp, "| Sum ; ", sum(comp))
        print("You won!")
        game_end = 0

    elif sum(comp) == 21:
        print("\nUser's cards : ", user, "| Sum ; ", sum(user))
        print("Comp's cards : ", comp, "| Sum ; ", sum(comp))
        print("You lost!")
        game_end = 0

    return user, comp, game_end


# This is for after first 2 cards already drawn -- for user
def ace_check_user(user):
    if 11 in user and sum(user) > 21:
        user.pop(user.index(11))
        user.append(1)
    return user


# This is for after first 2 cards already drawn -- for comp
def ace_check_comp(comp):
    if 11 in comp and sum(comp) > 21:
        comp.pop(comp.index(11))
        comp.append(1)
    return comp

# Asking for if user wants to draw another card
def draw_another_card_user():
    while True:
        user_input = input("\nDo you want to draw another card? (y/n) : ").lower()
        if user_input == "y" or user_input == "n":
            break
        else:
            print("Invalid input. Please try again.")
    return user_input


def comp_drawing_cards(comp):
    while True:
        if sum(comp) <= 16:
            comp.append(deal_card())
            comp = ace_check_comp(comp)
        else:
            break
    return comp


def user_drawing_cards(user, comp, game_end):
    if game_end != 0:
        while True:
            user_input = draw_another_card_user()
            if user_input == "y":
                user.append(deal_card())
                user = ace_check_user(user)
                print("\nUser's cards : ", user, "| Sum ; ", sum(user))
                print("Comp's cards : ", [comp[0]] + ["*"])

                if sum(user) > 21:
                    print("You past 21, You lost!.")
                    game_end = 0
                    break
                elif sum(user) == 21:
                    print("You got 21! Dealer's turn...")
                    comp = comp_drawing_cards(comp)
                    break

            elif user_input == "n":
                comp = comp_drawing_cards(comp)
                break

    return user, comp


def compare(user, comp, game_end):

    if game_end != 0:

        if sum(user) == 21:
            print("\nUser's cards : ", user, "| Sum ; ", sum(user))
            print("Comp's cards : ", comp, "| Sum ; ", sum(comp))
            print("You won!")

        elif sum(comp) == 21:
            print("\nUser's cards : ", user, "| Sum ; ", sum(user))
            print("Comp's cards : ", comp, "| Sum ; ", sum(comp))
            print("You lost!")

        elif sum(user) > 21:
            print("\nUser's cards : ", user, "| Sum ; ", sum(user))
            print("Comp's cards : ", comp, "| Sum ; ", sum(comp))
            print("You lost!")

        elif sum(comp) > 21:
            print("\nUser's cards : ", user, "| Sum ; ", sum(user))
            print("Comp's cards : ", comp, "| Sum ; ", sum(comp))
            print("You won!")

        elif sum(user) == sum(comp):
            print("\nUser's cards : ", user, "| Sum ; ", sum(user))
            print("Comp's cards : ", comp, "| Sum ; ", sum(comp))
            print("Game draw!")

        elif sum(user) < sum(comp):
            print("\nUser's cards : ", user, "| Sum ; ", sum(user))
            print("Comp's cards : ", comp, "| Sum ; ", sum(comp))
            print("You lost!")

        elif sum(user) > sum(comp):
            print("\nUser's cards : ", user, "| Sum ; ", sum(user))
            print("Comp's cards : ", comp, "| Sum ; ", sum(comp))
            print("You won!")



def game():
    user, comp = first_2_cards()
    user, comp, game_end = first_2_cards_check(user, comp)
    user, comp = user_drawing_cards(user, comp, game_end)
    compare(user, comp, game_end)

def blackjack():

    print(f"{BlackJack_game_logo}\n")
    reset_deck()
    game()

    while True:
        cont_game = input("\nDo you want to play again? (y/n) : ").lower()
        if cont_game == "y":
            print("\n"*20)
            print(f"{BlackJack_game_logo}\n")
            reset_deck()
            game()
        elif cont_game == "n":
            break
        else:
            print("Invalid input. Please try again.")

blackjack()