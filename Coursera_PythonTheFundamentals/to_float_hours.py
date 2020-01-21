#!/usr/bin/env python3


def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes and seconds.

    Preconditions: 0 <= minutes < 60  and  0 <= seconds < 60
    Divide mins by 60 = hours.
    Divide secs by 3600 = hours.

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """
    return hours + (minutes / 60) + (seconds / 3600)


Ans = to_float_hours(2, 45, 9)
print(Ans)

