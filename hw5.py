import random
import time
'''
Problem 1
'''
# Due next thursday
while(True):
    player_1_points = {}
    player_2_points = {}

    player_1 = input("Player 1 what is your name?: ")
    player_2 = input("Player 2 what is your name?: ")

    player_1 = str(player_1)
    player_2 = str(player_2)

    print(player_1"its your turn")

    time.sleep(2)

    player_1_roll = random.randint(1,6)
    print(player_1_roll)

    time.sleep(1)

    print(player_2" its your turn")

    time.sleep(2)

    player_2_roll = random.randint(1,6)
    print(player_2_roll)

    time.sleep(1)

    if(player_1_roll > player_2_roll):
        print("Player 1 you earned 1 point")
        player_1_points.append(1)
    elif player_1_roll < player_2_roll:
        print("player 2 you earned 1 point")
        player_2_points.append(1)
    elif player_1_roll == player_2_roll:
        print("It is a tie")

    time.sleep(2)

    print("player 1 your points are")
    print(player_1_points)

    time.sleep(2)

    print("player 2 your points are")
    print(player_2_points)

    time.sleep(2)

    game_round = 3 + 2

    print("player 1 would you like to play to "game_round)
    time.sleep(1)
    print("Please print yes or no")
    player_1_answer = input(">")

    print("Player 2 would you like to play to "game_round)
    time.sleep(1)
    print("Please print yes or no")
    player_2_answer = input(">")

    if (player_1_answer == player_2_answer):
        print("we will play to ")
    else:
        print("good game!")
        break