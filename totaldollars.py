#!/usr/bin/env python3

# Calculate the amount of money interactively.

# Use 'input' to get info from the user.
nOnes = input("How many ones do you have? ")
nFives = input("How many fives do you have? ")
nTens = input("How many tens do you have? ")
nTwenties = input("How many twenties do you have? ")

# Use 'int' to convert the inputted strings to integer values before multiplying.
total = int(nOnes) +  (int(nFives) * 5) + (int(nTens) * 10) + (int(nTwenties) * 20)

# Use 'str' to convert to a string, then concatenate on a decimal point and zeros.
totalAsString = str(total) + ".00"

# Concatenate dollar sign and strings, and print.
print("You have $" + totalAsString)
