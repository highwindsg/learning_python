#!/usr/bin/env python3


def traffic_report(light):
    if light == "red":
        return "stop"
    elif light == "yellow":
        return "slow"
    elif light == "green":
        return "go"


print(traffic_report("yellow"))