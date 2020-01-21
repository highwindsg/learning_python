#!/usr/bin/env python3


def to_24_hour_clock(hours):
    return hours % 24


def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours
    away from UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """

    utc_time = time - utc_offset
    result = to_24_hour_clock(utc_time)
    return result


Ans = time_to_utc(-1, 0.0)
print(Ans)

