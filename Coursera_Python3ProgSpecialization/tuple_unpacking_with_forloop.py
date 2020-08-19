#!/usr/bin/env python3

"""
Unpacking Into Iterator Variables.
Multiple assignment with unpacking is particularly useful when
you iterate through a list of tuples. You can unpack each tuple
into several loop variables.
"""

authors = [
            ("Paul", "Resnick"),
            ("Brad", "Miller"),
            ("Lauren", "Murphy")
            ]
print(authors)
print(type(authors))
print("")

for first_name, last_name, in authors:
    print("first name:", first_name, "last_name:", last_name)

print("")

