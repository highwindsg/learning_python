#!/usr/bin/env python3

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find("@")
print(atpos)    # Prints out the index position of '@'.

sppos = data.find(" ", atpos)
print(sppos)    # Prints out the index position of the first ' ' empty space.

host = data[atpos+1 : sppos]    # From var 'data', slice from index one slice after 'atpos',
                                # and up to but does not include the 'sppos' which is the first empty white space.
                                # Then assign it to new var 'host'.
print(host)
