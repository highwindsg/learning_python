#!/usr/bin/env python3


def convert_to_minutes(num_hours):
    result = num_hours * 60
    return result


hours_asleep = 5
minutes_asleep = convert_to_minutes(hours_asleep)
print("I'm still tired.")

