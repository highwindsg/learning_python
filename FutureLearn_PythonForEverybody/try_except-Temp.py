#!/usr/bin/env python3

inp = input("Enter Fahrenheit Temperature: ")

try:
    fahr = float(inp)
    cel = (fahr - 32) * 5.0 / 9.0
    print(cel)
except ValueError:
    print("Non-numeric value detected. Please re-run script and enter a number.")

