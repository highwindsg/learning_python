#!/usr/bin/env python3

# This function just prints a line of asterisks followed by a blank line.
def separateRuns():
    print("***************")
    print("")

def getGroceries(item1, item2, item3, item4):
    print(item1)
    print(item2)
    print(item3)
    print(item4)
    separateRuns()  # calling another function

# Main code starts here.
mustGet = "paper plates"
mustAlsoGet = "chocolate candy bars"
getGroceries(mustGet, mustAlsoGet, "lettuce", "cat food")
