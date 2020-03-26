#!/usr/bin/env python3


def mystery(lst):
    # total = 0
    for sublist in lst:
        total = 0
        for num in sublist:
            total = total + num

    return total


print(mystery([[10, 20], [20], [40, 10]]))

"""
Answer is 50.
Notice that total gets reset to 0 before each inner loop,
so when we return total, it will only contain the sum of the
items in the last sublist passed in.

If we wanted the total over all sublists, we would have to move
total=0 to before the first for loop. (eg. in line 5)
"""

