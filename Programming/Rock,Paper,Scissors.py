#Imports
from random import*
import time


choice = input("Rock,Paper or Scissors?")

choice = choice.upper()

if choice == "ROCK":
    print("You have chosen ROCK")
    time.sleep(1)
    program_choice = randint(1,3)
    if program_choice == 1:
        program_choice = "ROCK"
    elif program_choice == 2:
        program_choice = "PAPER"
    elif program_choice == 3:
        program_choice = "SCISSORS"

if choice == "PAPER":
    print("You have chosen ROCK")
    time.sleep(1)
    program_choice = randint(1,3)
    if program_choice == 1:
        program_choice = "ROCK"
    elif program_choice == 2:
        program_choice = "PAPER"
    elif program_choice == 3:
        program_choice = "SCISSORS"

if choice == "SCISSORS":
    print("You have chosen ROCK")
    time.sleep(1)
    program_choice = randint(1,3)
    if program_choice == 1:
        program_choice = "ROCK"
    elif program_choice == 2:
        program_choice = "PAPER"
    elif program_choice == 3:
        program_choice = "SCISSORS"
    
