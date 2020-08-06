# Imports

import random
import time
import sys

# -------------------#

# Card Values

Jack = 10

King = 10

Queen = 10

Ace = 1

# --------------------#

# Standard 52-card Deck

Cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, Jack, Jack,
         Jack, Jack, Queen, Queen, Queen, Queen, King, King, King, King, Ace, Ace, Ace, Ace]

# --------------------#

Hit_Choices = ["Hit", "H", "h", "hit", "iht", "thi", "ith", "tih", "hti"]

# Player & Dealer Decks

Player_Cards = []
Dealer_Cards = []

count = 1


# --------------------#

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


# --------------------#

# Starting Hand
for i in range(2):
    getcard_Player()
    getcard_Dealer()

# --------------------#

# First Hand

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

# --------------------#

# Hit or Stand?

for i in range(20):
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
        print("Your total is... {}".format(sum(Player_Cards)))
        time.sleep(1)
        gap()
        break

print("It is now the Dealer's turn.")
gap()
time.sleep(1)
print("The dealer's cards are {}".format(Dealer_Cards))
gap()
time.sleep(1)
Dealer_Total = sum(Dealer_Cards)
if (Dealer_Total) <= 16:
    count = 0

while count == 0:
    time.sleep(1)
    gap()
    print("The Dealer is drawing...")
    getcard_Dealer()
    gap()
    time.sleep(1)
    print("The Dealer's cards are {}".format(Dealer_Cards))
    gap()
    time.sleep(1)
    print("The dealer's total is {}".format(sum(Dealer_Cards)))
    Dealer_Total = sum(Dealer_Cards)
    if (Dealer_Total) >= 17:
        count = 1
else:
    time.sleep(1)

if (Dealer_Total) > 21:
    time.sleep(1)
    gap()
    print("Dealer has bust.")
    time.sleep(1)
    gap
    print("You have won")
    sys.exit('GAME OVER')

if (Dealer_Total) >= 17 and (Dealer_Total) <= 21:
    time.sleep(1)
    gap()
    print("Dealer has chosen to stand")
    time.sleep(1)
    gap()
    print("Comparing totals...")
    time.sleep(1)
    gap()
    print("Your total is... {}".format(sum(Player_Cards)))
    time.sleep(1)
    gap()
    print("The Dealer's total is...{}".format(sum(Dealer_Cards)))
    count = 1

if (Dealer_Total) > (Player_Total):
    time.sleep(1)
    gap()
    print("The Dealer has won.")
    sys.exit('GAME OVER')
if (Dealer_Total) < (Player_Total):
    time.sleep(1)
    gap()
    print("You have won.")
    sys.exit('CONGRATS')
if (Dealer_Total) == (Player_Total):
    time.sleep(1)
    gap()
    print("Both counts are the same, it is a draw.")
    sys.exit('GAME OVER')

# -------------------

# Rules:

# One [52] deck

# Points wagered before the match from 2 - 500

# The deal - 2 face up for players, 1 face up and 1 face down for dealers

# If dealers total is 17 or more it must stand. It is under they must take a card. If dealers ace bring total to 17 then it must be counted as 11.

# Naturals - Ace + 10, players get x1.5 bet, dealers gets bet unless a tie occurs.

# Soft hand - Ace + any other card than ten, If you draw even more and bust you can count the ace as one

# Splitting Pairs - If a player first gets two cards they can split to put the amount original bet one card and and equal bet on the other. If its two aces one card is given for each ace and after the player cannot draw again

# Attempt to get to 21 or under, bust if it is over

# Winner wins
