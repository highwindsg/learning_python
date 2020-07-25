#!/usr/bin/env python3

# Create a dict of items.
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print(inventory)
print("")

# Delete an item in a dict.
del inventory["pears"]
print(inventory)
print("")

# Update the value for an item in a dict.
inventory["durians"] = 90
print(inventory)
print("")

# Count the length or number of items in a dict.
numItems = len(inventory)
print(numItems)
print("")
#print(type(inventory.keys()))