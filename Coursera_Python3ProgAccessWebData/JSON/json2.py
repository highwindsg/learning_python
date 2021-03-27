#!/usr/bin/env python3

import json


# Below is a JSON data represented as a list with two nested dictionaries.
input = '''[
    {
        "id": "001",
        "x": "2",
        "name": "Chuck"
    },
    {
        "id": "009",
        "x": "7",
        "name": "Chuck"
    }
]'''

info = json.loads(input)    # Use the '.loads()' func from json library and parse in the var obj 'input'.
# And then assign it to var 'info'.
print(type(info))
print("User count:", len(info)) # From 'info' get its length.
print("")

for item in info:
    print("Name:", item["name"])    # Get the key value of item tag 'name'.
    print("Id:", item["id"])    # Get the key value of item tag 'id'.
    print("Attribute of x:", item["x"]) # Get the key value of item tag 'x'.
    print("")
    