#!/usr/bin/env python3

"""
Define a function called info with the following required parameters:
name, age, birth_year, year_in_college, and hometown.
The function should return a tuple that contains all the inputted
information.
"""

def info(name, age, birth_year, year_in_college, hometown):
    return name, age, birth_year, year_in_college, hometown


print(info("Jon", 22, 1945, 1960, "Georgetown"))
