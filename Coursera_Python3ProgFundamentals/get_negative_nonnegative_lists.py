#!/usr/bin/env python3


def get_negative_nonnegative_lists(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1, 3, 5], [2, -4, 5], [4, 0, 8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # CODE MISSING HERE
            val = L[row][col]
            if val < 0:
                neg.append(val)
            else:
                nonneg.append(val)

    return (neg, nonneg)


print(get_negative_nonnegative_lists([[-1, 3, 5], [2, -4, 5], [4, 0, 8]]))

