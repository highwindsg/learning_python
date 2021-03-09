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

info = json.loads(input)
print(type(info))
print("User count:", len(info))
print("")

for item in info:
    print("Name:", item["name"])
    print("Id:", item["id"])
    print("Attribute of x:", item["x"])
    print("")
    