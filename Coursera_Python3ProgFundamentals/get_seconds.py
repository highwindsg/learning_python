#!/usr/bin/env python3


def get_seconds(seconds):
    """ (int) -> int

    Seconds is a number of seconds since midnight.
    Return the number of seconds that have elapsed since midnight.

    >>> get_seconds(3800)
    20
    >>> get_seconds(7600)
    40
    """
    seconds_after_midnight = seconds % (3600 * 24)
    result = seconds_after_midnight % 60
    return result


Ans = get_seconds(3800)
print(Ans)

