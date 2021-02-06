#!/usr/bin/env python3

import image


img = image.Image("luther.jpg")

print("The image has a width of", img.getWidth(), "pixels.")
print("The image also has a height of", img.getHeight(), "pixels.")
print("")

# Return the pixel at col 45, row 86.
p = img.getPixel(45, 55)

# And then get the pixel's color value of var 'p'.
print("Image p's corresponding RGB color value is",
      p.getRed(),
      p.getGreen(),
      p.getBlue(),
      ".")
print("")
