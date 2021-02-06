#!/usr/bin/env python3

import image

p = image.Pixel(45, 76, 200)
print(p.getRed())
print("")

p.setRed(66)
print(p.getRed())
print("")

p.setBlue(p.getGreen())
print(p.getGreen(), p.getBlue())
print("")

p2 = image.Pixel(50, 0, 0)
print(p2)
