# DND Like Game, yes title in progress, made by Lucas Potter
# I couldn't care if you ctrl-c ctrl-v this entire thing as long as i get some credit
# Not just the title in progress, it's the whole thing

import time
import random

def diceRoll():
    x = int(random.uniform(1,20))
    print("You rolled a...")
    time.sleep(1.5)
    print(x)
    
def check(answer,correctAnswer,customEndLine):
    answerPublic = answer
    if answer == correctAnswer:
        print("Great!")
    else:
        print(customEndLine)

def startGame():
    name = input("What is your character's name?")
    print(name, ". I like that name.")
    time.sleep(1.5)
    print("What is", name, ", a wizard, a warrior, or a bard?")
    time.sleep(2)
    print("Wizards use spells, warriors use swords, and bards try to avoid violence.")
    time.sleep(3)
    print("Make sure to spell it exactly like shown when you enter it.")
    time.sleep(2)
    title = input("So, what will they be?")
    time.sleep(1)
    print(name, "is going to go on a grand adventure!")
    location = input("But, where will they go?")
    time.sleep(1)
    print("WONDERFUL!", name, "the", title, "will go on a grand adventure to", location)
    input("Press the ENTER key to continue your adventure!")

print("Hello! This is a DND like game which I made while I was bored during the COVID-19 lockdown.")
time.sleep(3)
print("Just a note: all things that ask for Y or N need to be lowercase.")
time.sleep(2)
print("Bonus note: There's no save. Exit out and everything disappears.")
time.sleep(2)
print("Anyway, let's get a test done. Make sure things are working.")
time.sleep(2)
input("Push the enter key. Something should show up similar to \"You rolled a *insert random number here*\".")
diceRoll()
testResult = input("Something showed up, right? Y/N")

if testResult == "y":
    playedBefore = input("Great! One more thing: have you played before? Y/N")
    if playedBefore == "y":
        name = input("Wonderful! Who was your character?")
        time.sleep(1.5)
        title = input("What was his title? Wizard, warrior, or bard?")
        time.sleep(1.5)
        location = input("Lastly, where was their adventure?")
        time.sleep(1.5)
        print("Great! Let's hop into it.")
    else:
        startGame()
else:
    print("Crap. Problem with the code. Contact the author @ thechamp190@gmail.com")
# qwerty
