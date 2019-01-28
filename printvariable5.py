#!/usr/bin/env python3

age = int(input("Enter your age: "))

if age <= 12:
    print("You're still a child.")
elif age <= 21:
    print("You're a teenager.")
elif age <= 45:
    print("You're an adult.")
else:
    print("You're getting old!")
