#!/usr/bin/env python3

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

for key in inventory.keys():
    print(key)

print("")

for key in inventory.keys():
    print(key, "has the value", inventory[key]) # We want the value of the
                                                # var key.

print("")

# To get the keys into a list.
keys = list(inventory.keys())   # Use the .keys() method on dict.
print(keys)
print("")

# Assign to var 'events' a list of the keys from dict 'medal_events'.
medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
# Using the .keys() method on dict to create the list.
events = list(medal_events.keys())
print(events)
print("")

# Create a list of the countries that are in the dictionary 'golds',
# and assign that list to the variable name 'countries'.
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries = list(golds.keys())
print(countries)
print("")

# Printing out the values only in a list.
print(list(inventory.values()))
print("")

# Printing out the items of keys and values in a list as tuples.
print(list(inventory.items()))
print("")

# Mapping of item in a dict to its value.
for k in inventory:
    print("Got", k, "that maps", inventory[k])
print("")

# Check boolean value if an item is in a dict.
print("apples" in inventory)
print("cherries" in inventory)
print("")

# Check if an key item is in a dict.
if "bananas" in inventory:
    print(inventory["bananas"])
else:
    print("We have no bananas")
print("")

# Using .get() method to get the value of a key item.
print(inventory.get("apples"))
print(inventory.get("cherries"))    # This will result in None.
# Rather than showing None, can also use optional output as 0 or a text string.
print(inventory.get("cherries", "I don't have this item."))