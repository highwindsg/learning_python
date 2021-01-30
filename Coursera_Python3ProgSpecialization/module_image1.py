#!/usr/bin/env python3

"""
Create a pixel with 45 units of red, 76 units of green, and 200 units of blue.
We then print the current amount of red, change the amount of red, and finally,
set the amount of blue to be the same as the current amount of green.
"""

import image


p = image.Pixel(45, 76, 200)
print(p.getRed())
p.setRed(66)
print(p.getRed())
p.setBlue(p.getGreen())
print(p.getGreen(), p.getBlue())
