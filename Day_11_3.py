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

deck_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4


def card_start(deck_cards):
    return deck_cards.pop(random.choice(range(len(deck_cards))))


# bet
def bet():
    while True:
        try:
            bet_amount = int(input("How much would you like to bet? : "))
            if bet_amount > 0:
                break
        except ValueError:
            print("Please enter a number.")



# Card distribution

def card_distribution(card_deck):
    random.shuffle(deck_cards)

    player = []
    dealer = []
    dealer_to_show: list[str] = ["*"]

    player.append(card_start(deck_cards))
    dealer.append(card_start(deck_cards))
    player.append(card_start(deck_cards))
    dealer.append(card_start(deck_cards))
    dealer_to_show.append(random.choice(dealer))

    return player, dealer, dealer_to_show



def first_game():
    if sum(player) > 21:
        print(f"Dealer cards : {dealer}")
        print(f"You past over 21, You lost!")
    elif sum(player)> 21:
        print(f"Dealer cards : {dealer}")
        print(f"Dealer past over 21, You win!")
    elif sum(player) == sum(dealer):
        print(f"Dealer cards : {dealer}")
        print(f"Draw!")
    elif sum(player) == 21:
        print(f"Dealer cards : {dealer}")
        print(f"You win!")
    elif sum(dealer) == 21:
        print(f"Dealer cards : {dealer}")
        print(f"You lost!")



def second_game():
    while True:
        try:
            player_input = input("\nWho would you like to hit or stand? :").lower()
            if player_input == "hit":
                break
            if player_input == "stand":
                break
        except ValueError:
            print("\nPlease enter hit or stand.")
    return player_input









bet()
player, dealer, dealer_to_show = card_distribution(deck_cards)
print(f"Player cards : {player}")
print(f"Player cards : {dealer_to_show}")
first_game()
player_input = second_game()