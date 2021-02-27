#!/usr/bin/env python3

"""
A negative image simply means that each pixel will be the opposite of the original.
eg. if original red value was 50, then opposite or negative red value would be 255 - 50.
"""

import image


img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1, 15)     # setDelay(0) turns off animation.

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        
        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()
        
        newpixel = image.Pixel(newred, newgreen, newblue)
        
        img.setPixel(col, row, newpixel)
        
    img.draw(win)

win.exitonclick()