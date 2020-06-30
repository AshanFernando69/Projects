#Imports
from random import*
import webbrowser
import sys
import winsound
import time


#Play Background Music

#Start

winsound.PlaySound("Caveambience", winsound.SND_ASYNC)

#Functions
def pause():
    time.sleep(1)

def gap():
    print("")

"PLAY THIS PROGRAM WITH SOUND UP"

#Player/Mob stats.

PlayerHP = 100
PlayerATK = 10
TrainingDummy = 30
TrainingDummyATK = 5
PlayerEXP = 0
PlayerLVL = 0

#EXP system.(WIP)

if PlayerEXP == 100:
    PlayerLVL = PlayerLVL+1
    time.sleep(1)
    gap()
    print("You LVLed up! You are now LVL {}.".format(PlayerLVL))
    PlayerEXP = 0

if PlayerLVL == 1:
    PlayerHP = PlayerHP+10
    PlayerATK = PlayerATK+5
    time.sleep(2)
    gap()
    print("Your damage has increased by 5.")
    time.sleep(1)
    gap()
    print("Your base damage is now 5")
    time.sleep(1)
    gap()
    print("Your health has been increased by 10.")
    time.sleep(1)
    gap()
    print("You now have 110 HP.")

TowardLightChoices = ["South","south","Go south","go South","go south"]
FIRSTGIFTChoices = ["Yes","yes","Y","y","yeah","Yeah","YES"]


print (" You feel a sudden ache at the back of your head.... Feels like someone knocked you out.")
gap()
pause()
print(" You awaken in a dark cave...")
gap()
time.sleep(2)
print(" W...Why am I here?")
gap()
pause()
print("You sense a strong wave of heat from the South.")
gap()
pause()
print("You look around and find another path leading to the North.")
gap()

time.sleep(1)
TowardLight = input("Do you want to go North or South? ")

if TowardLight in TowardLightChoices:
    pause()
    gap()
    print("You go down the Southern path.")
    pause()
    winsound.PlaySound("hard_shoes_1-daniel_simon", winsound.SND_ASYNC)
    gap()
    print("It's getting hotter every step you take...")
    pause()
    winsound.PlaySound("11168390_dragon-roar_by_soundhills_preview", winsound.SND_ASYNC)
    gap()
    print ("Oh no!  It was a dragon.")
    pause()
    gap()
    print("You spend the rest of your afterlife as a pile of ashes shame no0b")
    time.sleep(2)
    webbrowser.open("https://res.cloudinary.com/teepublic/image/private/s--pWjikVkS--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_600,q_90,w_600/v1480428599/production/designs/877345_1.jpg")
    winsound.PlaySound(None, winsound.SND_ASYNC)
    sys.exit(0)

if TowardLight not in TowardLightChoices:
    pause()
    gap()
    print("You go down the Northern Path.")
    pause()
    winsound.PlaySound("hard_shoes_1-daniel_simon", winsound.SND_ASYNC)
    gap()
    PLAYERNAME = input("I forgot to ask, what is your name? ")
    pause()
    gap()
    print (PLAYERNAME)
    pause()
    gap()
    print("Hmmm, Interesting.")
    pause()
    gap()
    print("Oh yeah, I forgot to give you a weapon, there are dangerous monsters down here...")
    pause()
    gap()
    print("Do you accept the LVL 1 Wooden sword?")

gap()
FIRSTGIFT = input("YES or NO ")
    
if FIRSTGIFT not in FIRSTGIFTChoices:
    pause()
    gap()
    print("Whatever you say kid...")
    pause()
    gap()
    print("You get jumped by a Goblin from behind.")
    time.sleep(2)
    webbrowser.open("https://res.cloudinary.com/teepublic/image/private/s--pWjikVkS--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_600,q_90,w_600/v1480428599/production/designs/877345_1.jpg")
    sys.exit(0)
          
if FIRSTGIFT in FIRSTGIFTChoices:
     PlayerATK == PlayerATK+10
     pause()
     gap()
     print("....")
     pause()
     gap()
     print("You do know how to use a sword right?")
     gap()
     pause()
     print("*Sigh* I guess I can teach you the basics..")
     pause()
     gap()
     print("Let me spawn in a Training Dummy, he's significantly weaker than other creatures around here.")
     gap()
     pause()
     print("If you lose to the Training Dummy you should stop playing games, no joke you must be a bot.")
     pause()

 #This is my battle system.
    
for i in range(100):
    Attackmove = randint(1,9)
    time.sleep(1)
    gap()
    AttackGuess = int(input("Select a number between 1-9 to attack. "))

    if AttackGuess == Attackmove:
        time.sleep(1)
        winsound.PlaySound("Decapitation", winsound.SND_FILENAME)
        gap()
        print("You successfully landed a hit.")
        TrainingDummy = TrainingDummy-PlayerATK
        gap()
        print("TrainingDummy has {} HP remaining.".format(TrainingDummy)) 

    if AttackGuess-1 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("Decapitation", winsound.SND_FILENAME)
        TrainingDummy = TrainingDummy-PlayerATK
        gap()
        print("TrainingDummy has {} HP remaining.".format(TrainingDummy)) 
        
    if AttackGuess+1 == Attackmove:
        time.sleep(1)
        winsound.PlaySound("Decapitation", winsound.SND_FILENAME)
        gap()
        print("You successfully landed a hit.")
        TrainingDummy = TrainingDummy-PlayerATK
        gap()
        print("TrainingDummy has {} HP remaining.".format(TrainingDummy)) 
    
    if AttackGuess-2 == Attackmove:
        time.sleep(1)
        winsound.PlaySound("Decapitation", winsound.SND_FILENAME)
        gap()
        print("You successfully landed a hit.")
        TrainingDummy = TrainingDummy-PlayerATK
        gap()
        print("TrainingDummy has {} HP remaining.".format(TrainingDummy))
        
    if AttackGuess+2 == Attackmove:
        time.sleep(1)
        winsound.PlaySound("Decapitation", winsound.SND_FILENAME)
        gap()
        print("You successfully landed a hit.")
        TrainingDummy = TrainingDummy-PlayerATK
        gap()
        print("TrainingDummy has {} HP remaining.".format(TrainingDummy)) 

    if AttackGuess+3 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("350925__cabled-mess__hurt-c-08", winsound.SND_FILENAME)
        print("TrainingDummy countered!")
        time.sleep(1)
        gap()
        print("You took 5 DMG!")
        time.sleep(1)
        PlayerHP = PlayerHP - TrainingDummyATK
        gap()
        print("You have {} HP remaining.".format(PlayerHP))
        
    if AttackGuess-3 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("350925__cabled-mess__hurt-c-08", winsound.SND_FILENAME)
        print("TrainingDummy countered!")
        time.sleep(1)
        gap()
        print("You took 5 DMG!")
        time.sleep(1)
        PlayerHP = PlayerHP - TrainingDummyATK
        gap()
        print("You have {} HP remaining.".format(PlayerHP))

    if AttackGuess+4 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("Woosh-Mark_DiAngelo-4778593", winsound.SND_FILENAME)
        print("TrainingDummy easily dodged your attack.")

    if AttackGuess-4 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("Woosh-Mark_DiAngelo-4778593", winsound.SND_FILENAME)
        print("TrainingDummy easily dodged your attack.")        

    if AttackGuess+5 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("Woosh-Mark_DiAngelo-4778593", winsound.SND_FILENAME)
        print("TrainingDummy easily dodged your attack.")
        
    if AttackGuess-5 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("Woosh-Mark_DiAngelo-4778593", winsound.SND_FILENAME)
        print("TrainingDummy easily dodged your attack.")   

    if AttackGuess+6 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("Woosh-Mark_DiAngelo-4778593", winsound.SND_FILENAME)
        print("TrainingDummy easily dodged your attack.")

    if AttackGuess-6 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("Woosh-Mark_DiAngelo-4778593", winsound.SND_FILENAME)
        print("TrainingDummy easily dodged your attack.")

    if AttackGuess+7 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("Woosh-Mark_DiAngelo-4778593", winsound.SND_FILENAME)
        print("TrainingDummy easily dodged your attack.")

    if AttackGuess-7 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("Woosh-Mark_DiAngelo-4778593", winsound.SND_FILENAME)
        print("TrainingDummy easily dodged your attack.")

    if AttackGuess+8 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("60013__qubodup__whoosh", winsound.SND_FILENAME)
        print("TrainingDummy easily dodged your attack.")

    if AttackGuess-8 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("Woosh-Mark_DiAngelo-4778593", winsound.SND_FILENAME)
        print("TrainingDummy easily dodged your attack.")

    if AttackGuess+9 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("Woosh-Mark_DiAngelo-4778593", winsound.SND_FILENAME)
        print("TrainingDummy easily dodged your attack.")

    if AttackGuess-9 == Attackmove:
        time.sleep(1)
        gap()
        winsound.PlaySound("Woosh-Mark_DiAngelo-4778593", winsound.SND_FILENAME)
        print("TrainingDummy easily dodged your attack.")
        
    if PlayerHP == 0:
        gap()
        print("...I can't believe you actually lost... Please don't play any game again, I'm very disappointed.")
        gap()
        print("You died.")
        time.sleep(2)
        webbrowser.open("https://res.cloudinary.com/teepublic/image/private/s--pWjikVkS--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_600,q_90,w_600/v1480428599/production/designs/877345_1.jpg")
        winsound.PlaySound(None, winsound.SND_ASYNC)
        sys.exit(0)
        
    if TrainingDummy == 0:
        EXP = randint(100,100)
        gap()
        print("You have defeated the Training Dummy!")
        time.sleep(1)
        gap()
        print("You have gained {} EXP".format(EXP))
        PlayerEXP = PlayerEXP+EXP
        time.sleep(1)
        PlayerHP = 100
        gap()
        print("You have recovered your health.")
        if PlayerEXP == 100:
            webbrowser.open("https://cdn.dribbble.com/users/131028/screenshots/2928341/level_up_2_1.gif")
            PlayerLVL = PlayerLVL+1
            time.sleep(1)
            gap()
            winsound.PlaySound("126422__cabeeno-rossley__level-up", winsound.SND_FILENAME)
            time.sleep(1)
            print("You LVLed up! You are now LVL {}.".format(PlayerLVL))
            PlayerEXP = 0
            if PlayerLVL == 1:
                PlayerHP = PlayerHP+10
                PlayerATK = PlayerATK+5
                time.sleep(2)
                gap()
                print("Your damage has increased by 5.")
                time.sleep(1)
                gap()
                print("Your base damage is now 5")
                time.sleep(1)
                gap()
                print("Your health has been increased by 10.")
                time.sleep(1)
                gap()
                print("You now have 110 HP.")
                break

time.sleep(1)
print("Took you long enough.")
pause()
print("This game is still in development.")
pause()
print("Like,favourite,subscribe")

          


    

    
    



    
    
        



