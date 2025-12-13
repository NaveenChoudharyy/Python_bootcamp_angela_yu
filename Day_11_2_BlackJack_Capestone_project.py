import random

deck_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Removed '1' from deck because 11 becomes 1 automatically if needed.

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(deck_cards)


def calculate_score(cards):
    """Calculates score and handles the Ace (11 -> 1) logic."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 represents a natural Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def blackjack():
    print("--- NEW GAME ---")
    user_cards = []
    computer_cards = []
    is_game_over = False

    # 1. Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # 2. The User's Turn Loop
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        # Check for immediate end conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # ASK THE USER
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # 3. The Computer's Turn (Only runs if user hasn't busted)
    # The computer MUST draw if score is less than 17, and not a Blackjack (0)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # 4. Final Results
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Run the game
blackjack()