#!/usr/bin/env python3


def for_version(L):
    """ (list of number) -> number

    The for loop stops as soon as an even number is found,
    and the sum of all the previous numbers is returned.
    """

    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True

    return total


print(for_version([9, 7, 3, 19, 2, 5, 4]))
