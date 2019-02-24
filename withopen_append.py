#!/usr/bin/env python3

# To save the content of the file to a variable or container
# so that can use later in the program.
my_list = list()

with open("st1.txt", "r") as f:
    my_list.append(f.read())    # We read the output of the content to the
                                # empty list for use later in the program.

print(my_list)
