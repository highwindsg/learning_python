#!/usr/bin/env python3

"""
Write a program that will convert degrees celsius to degrees fahrenheit.
Formula: Celsius (°C) times 9/5 plus 32.
"""

Celsius = float(input("Enter degree celsius: "))
Fahrenheit = (Celsius * (9 / 5)) + 32
print(Celsius, "degrees Celsius is", Fahrenheit, "degrees Fahrenheit.")
print("")



"""
Ask the user for the temperature in Fahrenheit and store it in a variable call deg_f. 
Calculate the equivalent temperature in degrees Celsius and store it in def_c. 
Output a message to the user giving the temperature in Celsius.
Formula: Fahrenheit (°F - 32) * (5 / 9)
"""

deg_f = float(input("Enter temperature in Fahrenheit: "))
deg_c = (deg_f - 32) * (5 / 9)
print("For the given", deg_f, "degrees Fahrenheit, after conversion it is", deg_c, "degrees Celsius.")
print("")
