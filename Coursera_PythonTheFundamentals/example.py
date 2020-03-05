#!/usr/bin/env python3


def example(L):
    """ (list) -> list

    Return a list containing every third item from L starting at index 0.
    """

    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result


L = "DOLITTLE"
print(example(L))

