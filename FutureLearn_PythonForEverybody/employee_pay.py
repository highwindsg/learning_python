#!/usr/bin/env python3

try:
    hours = int(input("Enter hours worked: "))
    rate = float(input("Enter current hourly rate: "))
    print("Pay: ", hours * rate)
except ValueError:
    print("Error, please enter numeric input")

