#!/usr/bin/env python3


def is_even(num):
    """ (int) -> boolean

    Return whether num is even.

    >>> is_even(4)
    True
    >>> is_even(77)
    False
    """

#    if num % 2 == 0:
#        return True
#    else:
#        return False

    # Alternatively, can use the one line code below to replace the
    # four lines above, as it is the same.
    return num % 2 == 0


print(is_even(4))
print(is_even(77))

