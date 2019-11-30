#!/usr/bin/env python3

# https://www.youtube.com/watch?v=xHPmXArK6Tg&list=PLOgeKhf41meTmtKSF8IKOzFcfh28Ks7Cx&index=166&t=474s

# Python Text RPG
# Name: highwind.sg

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

##### Player Setup #####
class player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = "start" 
        
myPlayer = player()

##### Title Screen #####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()    # placeholder until written
    elif option.lower() == ("help"):
        help_menu()     # placeholder until written
    elif option.lower() == ("quit"):
        sys.exit()
        
    while option.lower() not in ["play", "help", "quit"]:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()    # placeholder until written
        elif option.lower() == ("help"):
            help_menu()     # placeholder until written
        elif option.lower() == ("quit"):
            sys.exit()
        
        
def title_screen():
    os.system("clear")
    print("############################")
    print("# Welcome to the Text RPG! #")
    print("############################")
    print("         - Play -           ")
    print("         - Help -           ")
    print("     copyright 2019         ")
    
    title_screen_selections()
    

def help_menu():
    print("############################")
    print("# Welcome to the Text RPG! #")
    print("############################")
    print("- Use up, down, left, right to move")
    print("- Type your commands to do them")
    print("- Use look to inspect something")
    print("- Good luck and have fun!")
    
    title_screen_selections()
    

##### GAME FUNCTIONALITY #####
def start_game():
    
    
    
##### MAP #####
"""
a1 a2 ...   # PLAYER STARTS AT b2
-------------
|  |  |  |  |   a4
-------------
|  |  |  |  |   b4 ...
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
"""

ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

solved_places = {"a1": False, "a2": False, "a3": False, "a4": False,
                "b1": False, "b2": False, "b3": False, "b4": False,
                "c1": False, "c2": False, "c3": False, "c4": False,
                "d1": False, "d2": False, "d3": False, "d4": False, 
                }

zonemap = {
    "a1": {
        ZONENAME = "Town Market",
        DESCRIPTION = "description"
        EXAMINATION = "examine"
        SOLVED = False
        UP = ""
        DOWN = "b1"
        LEFT = ""
        RIGHT = "a2"
    },
     "a2": {
        ZONENAME = "Town Entrance",
        DESCRIPTION = "description"
        EXAMINATION = "examine"
        SOLVED = False
        UP = ""
        DOWN = "b2"
        LEFT = "a1"
        RIGHT = "a3" 
    },    
     "a3": {
        ZONENAME = "Town Square",
        DESCRIPTION = "description"
        EXAMINATION = "examine"
        SOLVED = False
        UP = ""
        DOWN = "b3"
        LEFT = "a2"
        RIGHT = "a4" 
    },    
     "a4": {
        ZONENAME = "Town Hall",
        DESCRIPTION = "description"
        EXAMINATION = "examine"
        SOLVED = False
        UP = ""
        DOWN = "b4"
        LEFT = "a3"
        RIGHT = "" 
    },    
     "b1": {
        ZONENAME = "",
        DESCRIPTION = "description"
        EXAMINATION = "examine"
        SOLVED = False
        UP = "a1"
        DOWN = "a1"
        LEFT = ""
        RIGHT = "b2"
    },
    "b2": {
        ZONENAME = "Home",
        DESCRIPTION = "This is your home!"
        EXAMINATION = "Your home looks the same - nothing has changed."
        SOLVED = False
        UP = "a2",
        DOWN = "c2",
        LEFT = "b1",
        RIGHT = "b3",
    },  


}

##### GAME INTERACTIVITY #####
def print_location():
    print("\n" + ("#" * (4 + len(myPlayer.location))))
    print("# " + myPlayer.location.upper() + " #")
    print("# " + zonemap[myPlayer.position][DESCRIPTION] + " #")
    print("\n" + ("#" * (4 + len(myPlayer.location))))
    
    
def prompt():
    print("\n" + "===============================")
    print("< What would you like to do?)
    action = input("> ")
    acceptable_actions = ["move", "go", "travel", "walk", "quit", "examine", "inspect", "look"]
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ["move", "go", "travel", "walk"]:
        player_move(action.lower())
    elif action.lower() in ["examine", "inspect", "interact", "look"]:
        player_examine(action.lower())
        

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ["up", "north"]:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ["left", "west"]:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ["east", "right"]:
        destination = zonemap[myPlayer, location][RIGHT]
        movement_handler(destination)
    elif dest in ["south", "down"]:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()
    

##### GAME FUNCTIONALITY #####
def start_game():
    return
