#!/usr/bin/env python3


def to_24_hour_clock(hours):
    return hours % 24


def get_hours(seconds):
    """ (int) -> int

    seconds is a number of seconds since midnight.
    Return the number of hours that have elapsed since midnight.

    >>> get_hours(3600)
    1
    >>> get_hours(7400)
    2
    """
    hours = seconds // 3600
    result = to_24_hour_clock(hours)
    return result


Ans = get_hours(7400)
print(Ans)

