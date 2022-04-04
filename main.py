# while blackjack function
import random


def player_drawing():
    draw = random.choice(cards)
    player_hand.append(draw)


def computer_drawing():
    draw = random.choice(cards)
    computer_hand.append(draw)


def computer_final_draw():
    computer_sum = 0
    while computer_sum < 17:
        draw = random.choice(cards)
        computer_hand.append(draw)
        for item in computer_hand:
            computer_sum += item
    return computer_sum


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
player_sum = 0
computer_hand = []





# player draws 2 times
for i in range(0, 2):
    player_drawing()
# player sum of hand
for card in player_hand:
    player_sum += card
# computer draws 1 time
computer_drawing()
# display start of game
print(f"Your cards: {player_hand}, current score: {player_sum} \nComputer's first card: {computer_hand}")
# asks player to continue drawing
continue_play = input("Type 'y' to get another card, type 'n' to pass: ")

while continue_play:
    player_drawing()
    player_sum += player_hand[-1]
    print(f"Your cards: {player_hand}, current score: {player_sum} \nComputer's first card: {computer_hand}")
    if player_sum > 21:
        computer_final_draw()
        # while computer_sum < 17:
        #     computer_drawing()
        # for card in computer_hand:
        #     computer_sum += card
        print(f"\nYour final hand: {player_hand}, final score: {player_sum} \nComputer's final hand: {computer_hand},"
              f"final score: {computer_final_draw()}")
        print("You went over. You lose!")
        continue_play = False
    else:
        continue_play = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if continue_play == "n":
            continue_play = False

