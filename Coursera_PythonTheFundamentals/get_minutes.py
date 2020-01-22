#!/usr/bin/env python3


def get_minutes(seconds):
    """ (int) -> int

    Seconds is a number of seconds since midnight.
    Return the number of minutes that have elapsed since midnight.

    >>> get_minutes(3800)
    3
    >>> get_minutes(7600)
    6
    """
    minutes = seconds // 60
    result = minutes % 60
    return result


Ans = get_minutes(7600)
print(Ans)

