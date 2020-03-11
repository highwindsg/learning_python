#!/usr/bin/env python3


def shift_left(L):
    """ (list) -> NoneType

    Shift each item in L one position to the left and shift the first item to
    the last position.

    Precondition: len(L) >= 1

    >>> shift_left(['a', 'b', 'c', 'd'])
    """

    L = ["a", "b", "c", "d"]

    first_item = L[0]
#    print(len(L))
    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item


print(shift_left(["a", "b", "c", "d"]))

