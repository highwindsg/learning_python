#!/usr/bin/env python3

def gender(age, sex):
    if (age > 21) and (sex == "f"):
        return True

def printAnswer():
    if gender(age, sex):
        print("I wonder what she is wearing today.")
    else:
        print("Hey! She's under-age.")

age = int(input("Enter the age: "))
sex = input("Enter the gender: ")
printAnswer()
