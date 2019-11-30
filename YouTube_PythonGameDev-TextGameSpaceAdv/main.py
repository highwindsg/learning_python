#!/usr/bin/env python3

# name: Mr Doug McNally
# date: 2019-11-30
# description: tex-based space adventure game
# https://www.youtube.com/watch?v=miuHrP2O7Jw&list=PLOgeKhf41meTmtKSF8IKOzFcfh28Ks7Cx&index=165&t=0s

import random
import time

def displayIntro():
    print("It is the end og a long year of fighting space crominals")
    print("you came to crossroads on your trip home, one path leads home")
    print("where you will be handsomely rewarded for a job well done")
    print("and the other leads through a gamma ray burst that will disintegrate you")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2":  # input validation
        path = input("Which path will you choose? (1 or 2): ")
        
    return path

def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("there's an asteroid nearby that looks familiar, that must be a good sign...")
    time.sleep(2)
    print("But your skin begins to tingle...")
    print()
    time.sleep(2)
    
    correctPath = random.randint(1, 2)
    
    if chosenPath == str(correctPath):
        print("That tingling was just the feeling of admiration from the citizens of the galaxy!")
        print("Welcome home!")
    else:
        print("An extremely energetic burst of gamma rays pass through you")
        print("causing all of the atoms in your body to dis-associate")
        print("there is no record left of your existence.")
        
        

playAgain = "yes"
while playAgain =="yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice)   # choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")
