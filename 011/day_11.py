import random
import art


def deal_card():

    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)


def calculate_score(cards):

    score = 0
    ace_count = 0

    for card in cards:
        if card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            score += 11
            ace_count += 1
        else:
            score += int(card)

    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1

    if score == 21 and len(cards) == 2:
        return 0
    return score


def compare(user_score, computer_score):
    if user_score > 21:
        return "You went over. You lose! "
    if computer_score > 21:
        return "Opponent went over. You win! "
    if user_score == computer_score:
        return "Draw "
    if computer_score == 0:
        return "Lose, opponent has Blackjack "
    if user_score == 0:
        return "Win with a Blackjack "
    if user_score > computer_score:
        return "You win! "
    else:
        return "You lose "


def play_game():
    print(art.logo)
    print("Welcome to Blackjack!")

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\n   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()