#!/usr/bin/env python3

import image


img = image.Image("luther.jpg")

print("The image has a width of", img.getWidth(), "pixels.")
print("The image also has a height of", img.getHeight(), "pixels.")
print("")

# Return the pixel at col 45, row 55.
p = img.getPixel(45, 55)
# Return the pixel at col 30, row 100.
p2 = img.getPixel(30, 100)


# And then get the pixel's color value of var 'p' & 'p2'.
print("At pixel of column 45 and row 86, image p's corresponding RGB color value is",
      p.getRed(),
      p.getGreen(),
      p.getBlue(),
      ".")
print("")

print("At pixel of column 30 and row 100, image p2's corresponding RGB color value is",
      p2.getRed(),
      p2.getGreen(),
      p2.getBlue(),
      ".")
print("")
