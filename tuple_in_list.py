#!/usr/bin/env python3

# Storing tuples in a list.

# First create a empty list named locations.
locations = []

# Create a tuple to contain the longitude & latitude of LA and Chicago and
# assign it to the var of la and chicago respectively.
la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

# Then append the variable of the longitude & latitude to the initial empty
# list of 'locations'.
locations.append(la)
locations.append(chicago)

print(locations)

