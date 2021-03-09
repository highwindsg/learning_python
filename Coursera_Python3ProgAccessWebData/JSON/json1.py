#!/usr/bin/env python3

"""
JSON represents data as nested "lists" and "dictionaries".
"""

import json # Import module library 'json'.



data = '''{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide": "yes"
    }
}'''

# Use the func '.loads()' from JSON library and parse in var obj 'data'.
# And then assign it to var 'info'.
info = json.loads(data)
print(type(info))

print("Name:", info["name"])    # From 'info' get the key value of tag 'name'.
print("Tel number:", info["phone"]["number"])   # From 'info', get the key value of tag 'phone' -> of tag 'number'.
print("Hide:", info["email"]["hide"])   # From 'info', get the key value of tag 'email' -> of tag 'hide'.
print("")
