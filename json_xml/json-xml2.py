#!/usr/bin/env python3

# Building two dict xml inside a list.

import json

# Two xml data structure in two dict format, stored in a list, and assigned to var obj 'input'.
input = '''[
    {   "id": "001",
        "x": "2",
        "name": "Chuck"
    },
    {   "id": "009",
        "x": "7",
        "name": "Chuck"
    }
]'''

info = json.loads(input)    # From json module, use the .loads() method and pass in the input var of the list.
print(info)     # Print out the 'info' list.
print("User count:", len(info))     # Print the length of the info var obj.

for item in info:
    print("Name", item["name"])     # For the line item in the list dictionary, print out the values of
    print("Id", item["id"])         # key 'name', 'id' and 'x' which is the attribute.
    print("Attribute", item["x"])
