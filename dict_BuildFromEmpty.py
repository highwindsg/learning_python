#!/usr/bin/env python3

purse = dict()  # Create an empty purse dict.
purse["money"] = 12     # Insert into purse dict with index key of 'money' and value of '12'.
purse["candy"] = 3      # Insert into purse dict with index key of 'candy' and value of '3'.
purse["tissue"] = 75    # Insert into purse dict with index key of 'tissue' and value of '75'.
print(purse)    # Print out the purse dict.
print(purse["candy"])   # Print out the value of 'candy'.
purse["candy"] = purse["candy"] + 2     # Add 2 to the key of 'candy' and assign it back to
                                        # the key of 'candy' in the purse dict.
print(purse)    # Print out the purse dict again.
print("")

ddd = dict()    # Create an empty ddd dict.
ddd["age"] = 21     # Insert into ddd dict with index key of 'age' and value of '21'.
ddd["course"] = 182     # Insert into ddd dict with index key of 'course' and value of '182'.
print(ddd)      # Print out the ddd dict.
ddd["age"] = 23     # Change the value of key 'age' by assigning new value of '23' to the 'age' key.
print(ddd)      # Print out the new ddd.

jjj = {     # Create a dict 'jjj' and enter the keys abd values straightaway.
    "chuck": 1,
    "fred": 42,
    "jen": 100
}
print(jjj)      # Print out the jjj dict.
ooo = { }       # Set a dict 'ooo' with no keys or values.
print(ooo)      # Print out a empty dict.

