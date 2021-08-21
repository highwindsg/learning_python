#!/usr/bin/env python3

"""
The following is only an example (code will not work) and has a bug and is also hard to read.

What I'm trying to say is I'm safe and prepared from today's weather....

- if I have an umbrella...
- or if the rain isn't too heavy and I have a hood...
- otherwise, I'm still fine unless it's raining and it's a workday
"""

prepared_for_weather = have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

"""We can use parentheses to make it more readable."""

prepared_for_weather = have_umbrella or (rain_level < 5 and have_hood) or not (rain_level > 0 and is_workday)

"""We can put in even more parentheses to increase the readability."""

prepared_for_weather = have_umbrella or ((rain_level < 5) and have_hood) or (not (rain_level > 0 and is_workday))

"""We can also split it over multiple lines to emphasize the 3-part structure described above."""

prepared_for_weather = (
    have_umbrella
    or ((rain_level < 5) and have_hood)
    or (not (rain_level > 0 and is_workday))
)
