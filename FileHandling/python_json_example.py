#!/usr/bin/env python3

# json is a text format which stands for JavaScript Object Notation and is used for
# storing and exchanging data.

import json

# Create a dictionary with var 'a'.
a = {
    "name": "Max",
    "age": 22,
    "marks": [90, 50, 80, 40],
    "pass": True,
    "object": {
        "color": ("red", "blue")
    }
}

# Convert the Python dict var obj 'a' into json format by using the '.dumps()' method in json.
print(json.dumps(a))

# Can also use indentation to indent 4 spaces for var obj 'a' in the json format,
# and also sort the dictionary's key in alphabetical order.
print(json.dumps(a, indent = 4, sort_keys = True))

print("")

# Can also use the 'with open()' function to open a new json file and then save/write into it.
with open("demo.json", "w") as fh:
    fh.write(json.dumps(a, indent = 2))

print("")

# To read json values from a file by converting it into a dictionary first.
with open("demo.json", "r") as fh:
    json_str = fh.read()    # Read the content of var 'fh' and assign in to var 'json_str' as json is a string file.
    json_value = json.loads(json_str)   # Use the 'json.loads()' method, pass in 'json_str' var and assign it to new
                                        # a var 'json_value'.
    # print(type(json_value))   # Check the data type of 'json_value' to see that it is indeed of class dict.
    print(json_value["name"])   # From the dict 'json_value', get the key value of 'name' and print out.

print("")

# Converting any data type below into a json value.
print(json.dumps({"name": "Max", "age": 22}))
print(json.dumps(["1", "2"]))
print(json.dumps(("1", "2")))
print(json.dumps("Hello World"))
print(json.dumps(100))
print(json.dumps(15.56))
print(json.dumps(False))
print(json.dumps(True))
print(json.dumps(None))
