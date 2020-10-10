#!/usr/bin/env python3

"""
A program that turns a number of seconds into more human readable counts of 
hours, minutes, and seconds.
"""

str_seconds = input("Please enter the number of seconds you wish to convert: ")
total_secs = int(str_seconds)

# To get whole number of hours.
hours = total_secs // 3600
# To find the remainder after the hours are confirmed.
secs_still_remaining = total_secs % 3600
# To find the whole numbers of mins that can be made up by the remaining secs.
minutes = secs_still_remaining // 60
# Finally to find out what are the remainder secs.
secs_finally_remaining = secs_still_remaining % 60

print(
    "Hrs=", hours,
    "mins=", minutes,
    "secs=", secs_finally_remaining
)
