import art
import random
import os

print(art.logo)


def deal_card():
    '''Returns card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(deck):
    '''Takes list of card and returns its score'''
    if 11 in deck and 10 in deck and len(deck) == 2:
        return 0

    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
        return sum(deck)

    return sum(deck)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Its a draw !!! 😐"
    elif computer_score == 0:
        return "You lose, Computer has a black jack !!! 🤣"
    elif user_score == 0:
        return "You win, you have a black jack!!! 😘 😊 😇"
    elif user_score > 21:
        return "You lose !!! 😜 😁 🤣"
    elif computer_score > 21:
        return "You win !!! 😘 😊 😇"
    elif user_score > computer_score:
        return "You win!!! 😘 😊 😇"
    elif user_score < computer_score:
        return "You lose!!! 😜 😁 🤣"


def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"your cards {user_cards}, your score {calculate_score(user_cards)} 🙂 \n")

        print(f"Computer's first card {computer_cards[0]} 🤫 \n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else:
            does_user_want_card = input("do you want to draw another card (y or n):")
            if does_user_want_card == 'y':
                user_cards.append(deal_card())
                print(f"your cards {user_cards}, your score {calculate_score(user_cards)} 🙂 \n")
            else:
                game_over = True

        if computer_score != 0 and computer_score < 17:
            while computer_score != 0 and computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)

        print(f"computer cards {computer_cards}, computer score {calculate_score(computer_cards)} 😁 \n")

        print(compare(user_score, computer_score))
        game_over = True
    main()


def main():
    choice = input("Do you want to play a game of blackjack 😉 😁  ? (y or n):")

    if choice == 'y':
        os.system('cls')
        play_game()
    else:
        print("\nwhat ?? 😠 😡 🤬 !!! ")


main()
