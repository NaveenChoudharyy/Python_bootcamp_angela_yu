# BlackJack project


#importing required packages
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

print(BlackJack_game_logo)

deck = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10] * 4
# A (ace) can either be 1 or 11
# J, K and Q have value as 10

# Bets
def bet():
    while True:
        try:
            player_bet = input("Please enter your amount to bet : ")
            player_bet = float(player_bet)
            break
        except ValueError:
            print("You can only enter numbers.")
    return player_bet


'''--------------------------------------------------------------------------------------------'''

def cards_distribution(deck):
    player = []
    dealer = []
    dealer_to_show = ["*"]

    # Cards
    random.shuffle(deck)  # To shuffle the deck of cards

    # Distributing 2 cards to the player and 2 cards to the dealer from the deck of shuffled cards
    player.append(deck.pop(random.choice(range(0, len(deck)))))
    dealer.append(deck.pop(random.choice(range(0, len(deck)))))
    player.append(deck.pop(random.choice(range(0, len(deck)))))
    dealer.append(deck.pop(random.choice(range(0, len(deck)))))
    dealer_to_show.append(dealer[0])
    print(f"Player cards: {player}")
    print(f"Dealer cards: {dealer_to_show}")

    return player, dealer, dealer_to_show


'''--------------------------------------------------------------------------------------------'''


'''--------------------------------------------------------------------------------------------'''




def first_game(player, dealer, player_bet, dealer_to_show):

    if sum(player) > 21:
        player = [1, 11]

    elif sum(dealer) > 21:
        dealer = [1, 11]

    elif sum(player) == 21 and sum(dealer) == 21:
        print(f"Dealer cards: {dealer}")
        print(f"It's a tie!")
        print("You are in no profit no loss. Play again.\n")
        first_game(player, dealer, player_bet, dealer_to_show) # Recursion so that game can restart------------------------

    elif sum(player) == 21:
        print(f"Dealer cards: {dealer}")
        print(f"You win! Amount you win is ${player_bet*1.5}. Now your total amount is ${player_bet*1.5 + player_bet}.")

    elif sum(dealer) == 21:
        print(f"Dealer cards: {dealer}")
        print(f"Dealer wins! Amount you lost is ${player_bet}.")

def dealer_card(dealer):
    if sum(dealer) <= 16:
        dealer.append(deck.pop(random.choice(range(0, len(deck)))))
        dealer_card(dealer)
    return dealer


'''--------------------------------------------------------------------------------------------'''


def second_game():
    while True:
        try:
            player_input = input("\nSelect one of the following options (hit or stand) : ").lower()
            if player_input == "hit" or player_input == "stand":
                break
        except ValueError:
            print("\nInvalid input. You can select either Hit or Stand.")

    return player_input


'''--------------------------------------------------------------------------------------------'''


def player_hit(player):
    player.append(deck.pop(random.choice(range(0, len(deck)))))
    return player


'''--------------------------------------------------------------------------------------------'''


def repeat_loop(player, dealer, player_bet, dealer_to_show):
    player, dealer, player_bet, dealer_to_show = first_game(player, dealer, player_bet, dealer_to_show)
    return player, dealer, player_bet, dealer_to_show




def hit_or_stand(player, dealer, player_bet, dealer_to_show, player_input):

    if player_input == "stand":
        print(f"Sum of player's cards: {sum(player)}")
        print(f"Sum of dealer's cards: {sum(dealer)}")

        if sum(player) > 21:
            print(f"Player cards: {player}")
            print(f"Dealer cards: {dealer}")
            print("Your total is over 21. You busted!")
            print(f"You lost! Since in Blackjack, the Player goes first.")

        elif sum(dealer) > 21:
            print(f"Player cards: {player}")
            print(f"Dealer cards: {dealer}")
            print("Dealer's total is over 21. Dealer busted!")
            print(f"You win! Amount you win is ${player_bet}. Now your total amount is ${player_bet + player_bet}.")

        elif sum(player) == sum(dealer):
            print(f"Player cards: {player}")
            print(f"Dealer cards: {dealer}")
            print(f"It's a tie!")
            print("You are in no profit no loss. Play again.\n")
            # Do something for recursion
            player_bet = bet()
            player, dealer, dealer_to_show = cards_distribution(deck)
            dealer = dealer_card(dealer)
            player, dealer, player_bet, dealer_to_show = first_game(player, dealer, player_bet, dealer_to_show)
            player_input = second_game()


        elif sum(player) > sum(dealer):
            print(f"Player cards: {player}")
            print(f"Dealer cards: {dealer}")
            print(f"You win! Amount you win is ${player_bet}. Now your total amount is ${player_bet + player_bet}.")

        elif sum(player) < sum(dealer):
            print(f"Player cards: {player}")
            print(f"Dealer cards: {dealer}")
            print(f"Dealer wins! Amount you lost is ${player_bet}.")


    elif player_input == "hit":

        if sum(player) > 21:
            print(f"Player cards: {player}")
            print(f"Dealer cards: {dealer}")
            print("Your total is over 21. You busted!")
            print(f"You lost! Since in Blackjack, the Player goes first.")

        else:
            player = player_hit(player)
            print(f"Player cards: {player}")
            print(f"Dealer cards: {dealer_to_show}")
            first_game(player, dealer, player_bet, dealer_to_show)
            player_input = second_game()
            hit_or_stand(player, dealer, player_bet, dealer_to_show, player_input)


def blackjack():
    player_bet = bet()
    player, dealer, dealer_to_show = cards_distribution(deck)
    dealer = dealer_card(dealer)
    first_game(player, dealer, player_bet, dealer_to_show)
    player_input = second_game()
    hit_or_stand(player, dealer, player_bet, dealer_to_show, player_input)

blackjack()
