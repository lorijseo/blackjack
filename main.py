# while blackjack function
def blackjack_play():
    import random

    def player_drawing():
        draw = random.choice(cards)
        player_hand.append(draw)

    def computer_first_draw():
        draw = random.choice(cards)
        computer_hand.append(draw)

    # def computer_drawing():
    #     computer_sum = computer_hand[0]
    #     while computer_sum < 17:
    #         draw = random.choice(cards)
    #         computer_hand.append(draw)
    #         computer_sum += computer_hand[-1]
    #     return computer_sum

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = []
    player_sum = 0
    computer_hand = []
    # player draws 2 times
    for i in range(2):
        player_drawing()
    # player sum of hand
    for card in player_hand:
        player_sum += card
    # computer draws 1 time
    computer_first_draw()
    # display start of game
    print(f"Your cards: {player_hand}, current score: {player_sum} \nComputer's first card: {computer_hand}")
    # asks player to continue drawing
    continue_play = input("Type 'y' to get another card, type 'n' to pass: ")


    while continue_play:
        player_drawing()
        player_sum += player_hand[-1]
        if player_sum > 21:
            # if we have an ace, we can replace with a value of 1.
            computer_sum = computer_hand[0]
            while computer_sum < 17:
                computer_draw = random.choice(cards)
                computer_hand.append(computer_draw)
                computer_sum += computer_hand[-1]
            print(f"Your final hand: {player_hand}, final score: {player_sum} \nComputer's final hand: {computer_hand},"
                  f"final score: {computer_sum}")
            print("You went over. You lose!")
            continue_play = False
        else:
            print(f"Your cards: {player_hand}, current score: {player_sum} \nComputer's first card: {computer_hand}")
            continue_play = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if continue_play == "n":
                continue_play = False


blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
if blackjack == 'y':
    blackjack_play()
else:
    print("Byebye")