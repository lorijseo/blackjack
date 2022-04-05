from art import logo
import random


def blackjack_play():
    def player_drawing():
        draw = random.choice(cards)
        player_hand.append(draw)

    def computer_first_draw():
        draw = random.choice(cards)
        computer_hand.append(draw)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = []
    player_sum = 0
    computer_hand = []

    for i in range(2):
        player_drawing()
    for card in player_hand:
        player_sum += card

    if player_sum > 21:
        player_hand.remove(11)
        player_hand.append(1)
        print("One of your aces is now represented as a value of 1")

    computer_first_draw()

    print(f"Your cards: {player_hand}, current score: {player_sum} \nComputer's first card: {computer_hand}")
    continue_play = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if continue_play == 'y':
        continue_play = True
    else:
        continue_play = False

    while continue_play:
        player_drawing()
        player_sum += player_hand[-1]
        if player_sum > 21:
            if 11 in player_hand:
                ace_location = player_hand.index(11)
                player_hand.remove(11)
                player_hand.insert(ace_location, 1)
                player_sum -= 10
                print("Your ace is now represented as a value of 1")
                print(f"Your cards: {player_hand}, current score: {player_sum} \n"
                      f"Computer's first card: {computer_hand}")
                continue_play = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if continue_play == "n":
                    continue_play = False
            else:
                continue_play = False
        else:
            print(f"Your cards: {player_hand}, current score: {player_sum} \nComputer's first card: {computer_hand}")
            continue_play = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if continue_play == "n":
                continue_play = False

    computer_sum = computer_hand[0]
    while computer_sum < 17:
        computer_draw = random.choice(cards)
        computer_hand.append(computer_draw)
        computer_sum += computer_hand[-1]
        if computer_sum > 21:
            if 11 in computer_hand:
                ace_location = computer_hand.index(11)
                computer_hand.remove(11)
                computer_hand.insert(ace_location, 1)
                computer_sum -= 10

    print(f"Your final hand: {player_hand}, final score: {player_sum} \nComputer's final hand: {computer_hand},"
          f"final score: {computer_sum}")
    if player_sum > 21:
        print("You went over. You lose!")
    elif computer_sum > 21:
        print("Computer went over. You win!")
    elif player_sum > computer_sum:
        print("You win!")
    elif player_sum < computer_sum:
        print("You lose!")
    else:
        print("It's a draw!")


blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
if blackjack == 'y':
    print(logo)
    blackjack_play()
else:
    print("Byebye")