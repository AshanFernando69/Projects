import sys
import time


def gap():
    print(" ")


# Rules function

def rules():
    print("You and the dealer will be dealt two cards.")
    time.sleep(3)
    gap()
    print("One of the dealers cards will be hidden until your turn has ended.")
    time.sleep(3)
    gap()
    print("Your goal is to get your count to 21 or close to it, without going over.")
    time.sleep(3)
    gap()
    print("You can 'Hit' to draw a card and 'Stand' to end your turn.")
    time.sleep(3)
    gap()
    print("If you go over 21 you will 'Bust' and the dealer will win.")
    time.sleep(3)
    gap()
    print("You can 'Stand' when you are comfortable with your count.")
    time.sleep(3)
    gap()
    print("If the dealer's count is equal to or less than 16 he must draw a card")
    time.sleep(3)
    gap()
    print("If both the player and the dealer have not 'Bust' at the end of their turns")
    time.sleep(3)
    gap()
    print("The program will compare both counts and decide the winner.")
    time.sleep(3)
    gap()
    print("Time to play!")
    time.sleep(5)


# -----------------------#

# Rules section

rule_choices = ["Y", "y", "YES", "yes", "Yes"]

print("Welcome to my Blackjack simulation!")
gap()
time.sleep(3)
rules_question = input("Would you like to read the rules?")
gap()

if rules_question in rule_choices:
    rules()


# -----------------------#

def main():
    # Imports

    import random
    import time
    import sys
    # -----------------------#

    # Card Values

    jack = 10
    king = 10
    queen = 10
    ace = 1
    # -----------------------#

    # Standard 52-card Deck

    cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, jack, jack,
             jack, jack, queen, queen, queen, queen, king, king, king, king, ace, ace, ace, ace]
    # -----------------------#

    # Choices for the 'Hit' option

    Hit_Choices = ["Hit", "H", "h", "hit", "iht", "thi", "ith", "tih", "hti", "HIT"]

    Stand_Choices = ["Stand", "S", "s", "stand", "dnats", "STAND"]
    # -----------------------#

    # Player & Dealer Deck

    Player_Cards = []
    Dealer_Cards = []

    # -----------------------#

    # Functions

    def gap():
        print(" ")

    def getcard_Player():
        player_card = random.choice(cards)
        Player_Cards.insert(0, player_card)
        cards.remove(player_card)
        print(Player_Cards)

    def getcard_Dealer():
        dealer_card = random.choice(cards)
        Dealer_Cards.insert(0, dealer_card)
        cards.remove(dealer_card)
        print(Dealer_Cards)

    def playAgain():
        import time
        replay_choice = ["Yes", "YES", "y", "Y", "yes"]
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
    time.sleep(2)
    print("The dealer's cards are [X,{}]".format(Dealer_Cards[1]))
    gap()
    # -----------------------#

    # Hit or Stand?

    for i in range(100):
        time.sleep(1)
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
            gap()
            if Player_Total > 21:
                time.sleep(2)
                gap()
                print("You have bust.")
                gap()
                time.sleep(1.5)
                print("GAME OVER")
                gap()
                playAgain()
        elif FirstRoundChoice in Stand_Choices:
            print("You have chosen to stand")
            gap()
            time.sleep(1)
            gap()
            break
        else:
            print("That is not an option.")
            gap()

    # -----------------------#

    # Dealer's Turn

    print("It is now the dealer's turn.")
    gap()
    time.sleep(1)
    Dealer_Total = sum(Dealer_Cards)
    if (Dealer_Total) <= 16:
        count = 0

    while count == 0:
        time.sleep(2)
        print("The dealer is drawing...")
        getcard_Dealer()
        gap()
        time.sleep(2)
        print("The dealer's cards are {}".format(Dealer_Cards))
        gap()
        time.sleep(2)
        print("The dealer's total is {}".format(sum(Dealer_Cards)))
        gap()
        Dealer_Total = sum(Dealer_Cards)
        if Dealer_Total >= 17:
            count = 1
    if (Dealer_Total) > 21:
        time.sleep(1)
        gap()
        print("Dealer has bust.")
        time.sleep(2)
        gap()
        print("You have won")
        time.sleep(2)
        gap()
        print("CONGRATS")
        time.sleep(2)
        playAgain()

    if 17 <= Dealer_Total <= 21:
        time.sleep(1)
        gap()
        print("Dealer has chosen to stand")
        time.sleep(2)
        gap()
        print("Comparing totals...")
        time.sleep(2)
        gap()
        print("Your total is... {}".format(sum(Player_Cards)))
        time.sleep(2)
        gap()
        print("The dealer's total is...{}".format(sum(Dealer_Cards)))
        if (Dealer_Total) > (Player_Total):
            time.sleep(1)
            gap()
            print("The Dealer has won.")
            gap()
            time.sleep(2)
            print("GAME OVER")
            gap()
            time.sleep(2)
            playAgain()
        if (Dealer_Total) < (Player_Total):
            time.sleep(1)
            gap()
            print("You have won.")
            gap()
            time.sleep(2)
            print("Congrats.")
            gap()
            time.sleep(2)
            playAgain()
        if (Dealer_Total) == (Player_Total):
            time.sleep(1)
            gap()
            print("Both counts are the same, it is a draw.")
            gap()
            time.sleep(2)
            print("Better luck next time.")
            gap()
            time.sleep(2)
            playAgain()


# -----------------------#

# Replay Function

def playAgain():
    import time
    replay_choice = ["Yes", "YES", "y", "Y"]
    print(" ")
    replay_ans = input("Would you like to play again?")
    if replay_ans in replay_choice:
        print(" ")
        print("Restarting Program...")
        time.sleep(3)
        main()
    else:
        time.sleep(3)
        print(" ")
        sys.exit("Thanks for playing!")


main()

playAgain()
