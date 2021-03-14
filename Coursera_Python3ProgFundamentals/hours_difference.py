#!/usr/bin/env python3


def hours_difference(time1, time2):
    """ (number, numner) -> float

    Return the number of hours later that a time in secs
    time_2 is than a time in secs time_1.

    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """
    return (time2 - time1) / 60 / 60


print(hours_difference(1800.0, 1800.0))

