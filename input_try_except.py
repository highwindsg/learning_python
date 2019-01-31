#!/usr/bin/env python3

try:
    a = int(input("Type a number: "))
    b = int(input("Type another number: "))
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("Invalid input.")
