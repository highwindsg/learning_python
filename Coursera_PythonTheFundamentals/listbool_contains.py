#!/usr/bin/env python3


def contains(value, lst):
    """ (object, list of list) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>>contains ("moogah", [[70, "blue"], [1.24, 90, "moogah"], [80, 100]])
    True
    """

    found = False   # We have not yet found value in the list.

    for sublist in lst:
        if value in sublist:
            found = True
# Or
#    for i in range(len(lst)):
#        for j in range(len(lst[i])):
#            if lst[i][j] == value:
#                found = True

    return found


print(contains("moogah", [[70, "blue"], [1.24, 90, "moogah"], [80, 100]]))


