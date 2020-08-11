# Imports

import random
import time
import sys

# -----------------------#

# Card Values

Jack = 10

King = 10

Queen = 10

Ace = 1

# -----------------------#

# Standard 52-card Deck

Cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, Jack, Jack,
         Jack, Jack, Queen, Queen, Queen, Queen, King, King, King, King, Ace, Ace, Ace, Ace]

# -----------------------#

# Choices for the 'Hit' option

Hit_Choices = ["Hit", "H", "h", "hit", "iht", "thi", "ith", "tih", "hti"]

# -----------------------#

# Player & Dealer Deck

Player_Cards = []

Dealer_Cards = []


# -----------------------#

# Functions

def gap():
    print(" ")


def getcard_Player():
    player_card = random.choice(Cards)
    Player_Cards.insert(0, player_card)
    Cards.remove(player_card)
    print(Player_Cards)


def getcard_Dealer():
    dealer_card = random.choice(Cards)
    Dealer_Cards.insert(0, dealer_card)
    Cards.remove(dealer_card)
    print(Dealer_Cards)

# -----------------------#

#Starting Hand

for i in range(2):
    getcard_Dealer()
    getcard_Player()

# -----------------------#

#First Hand

Player_Total = sum(Player_Cards)
Dealer_Total = sum(Dealer_Cards)

print("Your cards are {}".format(Player_Cards))
gap()
time.sleep(2)
print("Your total is... {}".format(Player_Total))
gap()
time.sleep(1)
print("The dealer's cards are [X,{}]".format(Dealer_Cards[1]))
gap()

# -----------------------#

#Hit or Stand?

for i in range(100):
    time.sleep(1)
    gap()
    FirstRoundChoice = input("Would you like to 'Hit' or 'Stand'?")
    gap()
    time.sleep(1)
    if FirstRoundChoice in Hit_Choices:
        getcard_Player()
        print("Your cards are {}".format(Player_Cards))
        gap()
        time.sleep(1)
        Player_Total = sum(Player_Cards)
        print("This brings your total to... {}".format(Player_Total))
        if Player_Total > 21:
            gap()
            print("You have bust.")
            gap()
            sys.exit('Your count has exceeded 21.')

    if FirstRoundChoice not in Hit_Choices:
        print("You have chosen to stand")
        gap()
        time.sleep(1)
        gap()
        break
