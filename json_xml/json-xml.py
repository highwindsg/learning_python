#!/usr/bin/env python3

import json     # Import the JavaScript Object Notation (JSON) module.

# User information in xml format, and assigned to var 'data'.
# Format is similar to a dictionary's key:value pairing.
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

info = json.loads(data)     # From json module, use the .loads() method and pass in 'data' var obj,
                            # and assign it to var 'info'.
print("Name:",info["name"])     # Print out the value of 'name' slice, from 'info' var obj.
print("Hide:",info["email"]["hide"])    # Print out the value of slice 'email' and sub-slice value of 'hide'.