#!/usr/bin/env python3


def seconds_difference(time1, time2):
    """ (number, number) -> number

    Return the number of secs later that a time in secs
    time_2 is than a time in secs time_1.

    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """
    return time2 - time1


print(seconds_difference(1800.0, 1800.0))

