#!/usr/bin/env python3

jjj = {
    "chuck": 1,
    "fred": 42,
    "jen": 100
}

# Print out the dict as a list.
print(list(jjj))

# Print out only the keys from the dict.
print(jjj.keys())

# Print out only the values from the dict.
print(jjj.values())

# Print out the dict items and set them as a tuples in a list.
print(jjj.items())

print("")

"""
We can loop through the key-value pairs in a dict
using two iteration variables. (eg. 'aaa' and 'bbb')
Each iteration, the first var is the 'key',
and the second var is the corresponding 'value'
for the key.
"""
for aaa, bbb in jjj.items():
    print(aaa, bbb)
