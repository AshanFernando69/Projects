import sys


def main():
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

    def playAgain():
        import time
        replay_choice = ["Yes", "YES", "y", "Y","yes"]
        replay_ans = input("Would you like to play again?")
        if replay_ans in replay_choice:
            print("Restarting Program...")
            time.sleep(3)
            main()
        else:
            sys.exit("Thanks for playing!")

    # -----------------------#

    # Starting Hand
    for i in range(2):
        getcard_Dealer()
        getcard_Player()
    # -----------------------#

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
    # -----------------------#

    # Hit or Stand?

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

    # -----------------------#

    # Dealer's Turn

    print("It is now the dealer's turn.")
    gap()
    time.sleep(1)
    Dealer_Total = sum(Dealer_Cards)
    if (Dealer_Total) <= 16:
        count = 0
    while count == 0:
        time.sleep(1)
        gap()
        print("The dealer is drawing...")
        getcard_Dealer()
        gap()
        time.sleep(1)
        print("The dealer's cards are {}".format(Dealer_Cards))
        gap()
        time.sleep(1)
        print("The dealer's total is {}".format(sum(Dealer_Cards)))
        Dealer_Total = sum(Dealer_Cards)
        if (Dealer_Total) >= 17:
            count = 1
    if (Dealer_Total)>21:
        time.sleep(1)
        gap()
        print("Dealer has bust.")
        time.sleep(1)
        gap()
        print("You have won")
        time.sleep(2)
        sys.exit('CONGRATS')
        playAgain()

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
        print("The dealer's total is...{}".format(sum(Dealer_Cards)))
        if (Dealer_Total) > (Player_Total):
            time.sleep(1)
            gap()
            print("The Dealer has won.")
            gap()
            time.sleep(1)
            print("GAME OVER")
            playAgain()
        if (Dealer_Total) < (Player_Total):
            time.sleep(1)
            gap()
            print("You have won.")
            gap()
            time.sleep(1)
            print("Congrats.")
            playAgain()
        if (Dealer_Total) == (Player_Total):
            time.sleep(1)
            gap()
            print("Both counts are the same, it is a draw.")
            gap()
            time.sleep(1)
            print("Better luck next time.")

# -----------------------#

# Replay Function

def playAgain():
    import time
    replay_choice = ["Yes","YES","y","Y"]
    print(" ")
    replay_ans = input("Would you like to play again?")
    if replay_ans in replay_choice:
        print("Restarting Program...")
        time.sleep(3)
        main()
    else:
        time.sleep(3)
        sys.exit("Thanks for playing!")

main()

playAgain()
