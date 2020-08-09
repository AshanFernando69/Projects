#Imports

import random
import time
import sys

#-----------------------#

#Card Values

Jack = 10

King = 10

Queen = 10

Ace = 1

#-----------------------#

#Standard 52-card Deck

Cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, Jack, Jack, Jack, Jack, Queen, Queen, Queen, Queen, King, King, King, King, Ace, Ace, Ace, Ace]

#-----------------------#

#Choices for the 'Hit' option

Hit_Choices =  ["Hit","H","h","hit","iht", "thi", "ith", "tih", "hti"]

#-----------------------#

#Player & Dealer Deck

Player_Cards = []

Dealer_Cards = []

#-----------------------#

#Functions

def gap():
    print(" ")

def getcard_Player():
    player_card = random.choice(Cards)
    player_Cards.insert(0, Player_card)
    Cards.remove(player_card)
    print(Player_Cards)

def getcard_Dealer():
    dealer_card = random.choice(Cards)
    Dealer_Cards.insert(0, dealer_card)
    Cards.remove(dealer_card)
    print(Dealer_Cards)