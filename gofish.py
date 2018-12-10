from deck import deck
from player import player


'''
each player takes a turn, they can choose one card in their deck
and asks the player if they have that card

setup:
each player starts with 7 cards
if 4 or more people are playing you start with 5 cards
each player has a name
if they have all 4, then they get the points and drawback 7

if they don't have the card, then the asker draws a card

if you have a pair of cards you can remove those cards from
your deck

Game is over when draw pile is empty
'''
draw_pile = deck(True)
discard_pile = deck()

draw.pile.fan()
discard_pile.fan()

def setup():
    pass

def playgame():
    pass

playercount = int(input("How many people are playing?"))
players = {}

for current_player in range(playercount):
    players[input("Enter your name: ")] = player()

for current_player in players:
    player1 = len(players == 1)
    player2 = len(players == 2)
    player3 = len(players == 3)

    for player in players:
        
    # take turn
    # Asking whitch player you want by question
    # make a menu by looping through player keys
    # ask them if they have one of your cards
    # when they do increase player score
    # when they dont player draws from draw_pile
