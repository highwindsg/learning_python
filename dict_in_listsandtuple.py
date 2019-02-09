#!/usr/bin/env python3

# Storing a dictionary into a list and a tuple.

bday = {"Hemingway":
        "7.21.1899",
        "Fitzgerald":
        "9.24.1896"
        }

my_list = [bday]
print(my_list, "-- dictionary in a list")

my_tuple = (bday,)  # Even if a tuple has one item in it, you need to put a
                    # comma after it. That way Python can differentiate it
                    # from a number surrounded by parentheses.
print(my_tuple, "-- dictionary in a tuple")

