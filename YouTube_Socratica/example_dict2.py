#!/usr/bin/env python3

my_addr = {"Block": 200,
           "Floor unit": "10-228",
           "Street name": "Punggol Road",
           "Country": "Singapore"
           }

print(my_addr)
print(type(my_addr))
print("")

# Creating a dictionary straightaway using the dict constructor function.
my_addr3 = dict(Block=242,
                Floor_unit="08-24",
                Street_name="Ang Mo Kio, Ave 1",
                Country="Singapore"
                )

print(my_addr3)
print(type(my_addr3))
print("")

# Accessing values from two dictionaries.
print(my_addr["Block"])
print(my_addr3["Floor_unit"])

# Adding new key and value to the two dict.
my_addr["Region"] = "S. E. Asia"
my_addr3["Region"] = "S. E. Asia"
print(my_addr)
print(my_addr3)
print("")

# To print out a 'location' value though it does not exist in te dict, and use 'try and except' method to handle
# the error.

try:
    print(my_addr["location"])
except KeyError:
    print("The address does not contain the location infor.")
