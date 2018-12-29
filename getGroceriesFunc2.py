#!/usr/bin/env python3

# This function just prints a line of asterisks followed by a blank line.
def separateRuns():
    print("***************")
    print("")

def getGroceries(item1):
    print(item1)
    print("flour")
    print("sugar")
    print("squash")
    separateRuns()  # calling another function

# Main code starts here.
getGroceries("eggs")
getGroceries("beer")
getGroceries("apples")
