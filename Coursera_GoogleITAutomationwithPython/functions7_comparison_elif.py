#!/usr/bin/env python3

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must not be more than 15 characters long.")
    else:
        print("Valid username.")
        
        
print(hint_username("Johny Winter Hates Jazz"))
print("")

print(hint_username("Johny Depp"))
print("")



"""
The number_group function should return "Positive" if the number received is positive, "Negative" if it's negative, and "Zero" if it's 0.
"""

def number_group(number):
    if number > 1:
        return "Positive"
    elif number == 0:
        return "Zero"
    else:
        return "Negative"
    
    
print(number_group(4))
print("")

print(number_group(0))
print("")
