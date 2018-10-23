import random
import time
'''
Problem 1
'''
# Due next thursday

player_1_points = []
player_2_points = []


player_1 = input("Player 1 what is your name?: ")
player_2 = input("Player 2 what is your name?: ")

print("player 1 its your turn")

time.sleep(1)

player_1_roll = random.randint(1,6)
print(player_1_roll)

time.sleep(1)

print("player 2 its your turn")

time.sleep(1)

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