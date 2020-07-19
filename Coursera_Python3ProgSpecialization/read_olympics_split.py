#!/usr/bin/env python3

"""Using the split method, we can break each line into a list containing all
the fields of interest about the athlete. We can then take the values
corresponding to name, team and event to construct a simple sentence."""

olympicsfile = open("olympics.txt", "r")

for aline in olympicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olympicsfile.close()

