#!/usr/bin/env python3


def weather_report(temp):
    if temp >= 20:
        return "warm enough for ice cream"
    elif temp >= 0:
        return "above freezing"


print(weather_report(10))
print(weather_report(-5))
print(weather_report(30))
print(weather_report(20))

