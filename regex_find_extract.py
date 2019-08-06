#!/usr/bin/env python3

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find("@")  # Starting from index position 0, '@' is at index position 21.
print(atpos)

sppos = data.find(" ", atpos)   # And the empty space after index position 21 is at 31.
print(sppos)

hostname = data[atpos+1 : sppos]    # Only find the hostname by slicing var 'data'.
print(hostname)                     # Print out only the 'hostname'.

