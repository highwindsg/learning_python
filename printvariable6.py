#!/usr/bin/env python3

age = int(input("How old are you now? "))
retirement = 65 - age

if retirement < 10:
    print("You get to retire soon.")
else:
    print("You are still a long way to retirement!")
