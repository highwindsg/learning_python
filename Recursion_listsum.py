#!/usr/bin/env python3

def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


numList = (1, 3, 5, 7, 9)
print(listsum(numList))
