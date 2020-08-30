#!/usr/bin/env python3

"""
The sorted() function takes some optional parameters.
"""

L2 = ["Cherry", "Apple", "Blueberry"]

print(sorted(L2))   # Default sorting.
print("")

print(sorted(L2, reverse = True))   # Sort the reverse way by using
                                    # a optional param.
print("")

print(sorted(L2, reverse = False))  # This is the default even if
                                    # 'reverse = False' is not specified.
print("")


"""
Sort the list, lst from largest to smallest.
Save this new list to the variable lst_sorted.
"""

lst = [3, 5, 1, 6, 7, 2, 9, -2, 5]

lst_sorted1 = sorted(lst)   # Default sorting for numbers is smallest
                            # to largest.
print(lst_sorted1)

lst_sorted2 = sorted(lst, reverse = True)
print(lst_sorted2)
print("")
