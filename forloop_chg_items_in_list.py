#!/usr/bin/env python3

# Can use 'for loop' to change the items in a mutable iterable, like a list.

tv = [
"GOT",
"Narcos",
"Vice"
]

i = 0   # To keep track of the current item in the list using an index variable.
        # A var that holds an integer representing an index in an iterable.
for show in tv:
    new = tv[i]     # You use the index var to get the current item from the 'tv'
                    # list, which you then store in the variable 'new'.
    new = new.upper()   # Calling the upper case method on the value of var 'new'.
    tv[i] = new     # And then assigning the upper-cased value of var 'new' back into
                    # the index var of tv list.
    i += 1          # Finally you increment 'i' so you can look up the next item
                    # in the list for the next round of loop.

print(tv)

