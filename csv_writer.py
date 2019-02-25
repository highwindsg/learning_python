#!/usr/bin/env python3

import csv  # In order to convert the file object into a csv object, this module
            # has a method called 'writer'.

with open("st.csv", "w", newline='') as f:  # Create a new file 'st.csv' with write
                                            # permission and assign to 'f'.
    w = csv.writer(f,   # The 'writer' method accepts a file object and a delimiter,
                   delimiter=",")   # and then returns a csv object eg. 'w'.

    w.writerow(["one",      # The csv object (w) has a method called 'writerow'
                "two",      # that accepts a list as a param.
                "three"])

    w.writerow(["four",     # Every item item in the list gets written, separated by
                "five",     # the delimiter (,) which you pass to the 'writer' method
                "six"])     # to a row in the CSV file.

"""
As the 'writerow' method only creates one row, you have to call it twice
to create two rows. eg. line 9 and line 12.
"""
