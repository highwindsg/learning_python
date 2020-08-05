#!/usr/bin/env python3

"""
'schedule' is a dictionary where a class name is a key and its value is how many
credits it was worth. Go through and accumulate the number of credits that
have been earned so far and assign that to the variable 'total_credits'.
Do not hardcode.
"""

schedule = {
            "UARTS 150": 3,
            "SPANISH 103": 4,
            "ENGLISH 125": 4,
            "SI 110": 4,
            "ENS 356": 2,
            "WOMENSTD 240": 4,
            "SI 106": 4,
}

total_credits = 0   # Initialize accumulator var.
for course in schedule:
    total_credits = total_credits + schedule[course]

print(total_credits)
