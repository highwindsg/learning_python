#!/usr/bin/env python

import csv  # In order to convert the file object into a csv object, this module
            # has a method called 'writer'.

with open("st.csv", "r") as f:          # open the existing file with read permission.
    r = csv.reader(f, delimiter=",")    # The 'reader' method accepts a file and a delimiter
                                        # and assigns the csv object to 'r'.
    for row in r:               # Each time around the for loop, you call the 'join' method
        print(",".join(row))    # on a comma between each piece of data, and print the content.
