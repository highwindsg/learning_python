#!/usr/bin/env python3

"""
Flesh out the body of the print_seconds function so that it prints the total 
amount of seconds given the hours, minutes, and seconds function parameters. 
Remember that there are 3600 seconds in an hour and 60 seconds in a minute.
"""

def print_seconds(hours, minutes, seconds):
    print((3600 * hours) + (60 * minutes) + seconds)
    

# Func call to print out the total number of secs with given 1 hr, 2 mins and 3 secs.    
print_seconds(1, 2, 3)
print("")

