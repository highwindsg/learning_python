#!/usr/bin/env python3

precipitation = True
temperature = -3

if precipitation:
    if temperature > 0:
        print("Bring your umbrella!")
    else:
        print("Wear your boots and winter coat!")

if precipitation and temperature > 0:
    print("Bring your umbrella!")
elif precipitation:
    print("Wear your boots and winter coat!")

