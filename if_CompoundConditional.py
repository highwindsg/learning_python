#!/usr/bin/env python3

## https://www.youtube.com/watch?v=E-c0w5Latbc


myColor = input("Please input your color: ")
if myColor == "Red" or myColor == "red" or myColor == "RED":    # can try using myColor.lower()
    print("Your color is red")
if myColor != "Red" and myColor != "red" and myColor != "RED":
    print("Your color is not red")
    