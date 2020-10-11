#!/usr/bin/env python3

"""
Write a program that will convert tablespoons to teaspoons. 
This program will also need to get input from a user to see how many tablespoons 
should be converted and the result should be printed to the user.
"""

user_tablespoons = float(input("How many tablespoons should be converted?: "))
teaspoons = user_tablespoons * 3
print("Number of teaspoons: " + str(teaspoons))
print("")
