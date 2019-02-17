#!/usr/bin/env python3

# Using 'for loop' to move data between mutable iterables.
# Use two 'for loop' to take all the strings from two different lists,
# capitalize each char in them, and put them into a new list.

tv = [
"GOT",
"Narcos",
"Vice"
]

coms = [
"Arrested Development",
"friends",
"Always Sunny"
]

all_shows = []      # First create a new empty list.

for show in tv:
    show = show.upper()     # Upper-case the value in show and reassign it back
                            # to the variable show.
    all_shows.append(show)  # Then add (append) the value of the var show into
                            # the new list of 'all_shows'.

for show in coms:
    show = show.upper()     # Upper-case the value in show and reassign it back
                            # to the variable show.
    all_shows.append(show)  # Then add (append) the value of the var show into
                            # the new list of 'all_shows'.

print(all_shows)

