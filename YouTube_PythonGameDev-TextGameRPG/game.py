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

DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

solved_places = {}
