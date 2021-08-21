#!/usr/bin/env python3

"""
Define a function called 'sign' which takes a numerical argument
and returns -1 if it's negative, 1 if it's positive, and 
0 if it's 0.
"""

def sign(num):
    if num == 0:
        return 0
    elif num < 0:
        return -1
    elif num > 0:
        return 1
    
    
print(sign(5))
print(sign(-3))
print(sign(0))
print("")



"""
The boolean variables ketchup, mustard and onion represent whether a customer wants a 
particular topping on their hot dog. We want to implement a number of boolean functions 
that correspond to some yes-or-no questions about the customer's order. For example:
"""

def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    #return not ketchup and not mustard and not onion
    # Or,
    return not (ketchup or mustard or onion) # by factoring out the 'nots'.

def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup)

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (int(ketchup) + int(mustard) + int(onion)) == 1
    """We don't technically need to call int on the arguments. Just by doing addition 
    with booleans, Python implicitly does the integer conversion."""
    return (ketchup + mustard + onion) == 1
