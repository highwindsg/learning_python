#!/usr/bin/env python3

# Ask user to enter weight, can even in decimal points.
weight = float(input("Enter your weight in pounds: "))

# Multiply the weight input to pounds with formula.
weight_in_kg = weight * 0.45359237

# Then print out the weight in kg by converting the float back into str.
print("Your weight in kg is " + str(weight_in_kg) + "kg")

