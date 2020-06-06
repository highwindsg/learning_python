#!/usr/bin/env python3

try:
    score = float(input("Enter score: "))

    if score < 0.0:
        print("Error, please enter between 0.0 and 1.0")
    if score > 1.0:
        print("Error, please enter between 0.0 and 1.0")
    elif score >= 0.9:
        print("Grade A")
    elif score >= 0.8:
        print("Grade B")
    elif score >= 0.7:
        print("Grade C")
    elif score >= 0.6:
        print("Grade D")
    else:
        print("Grade F")


except ValueError:
    print("Bad score")

