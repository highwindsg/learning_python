#!/usr/bin/env python3

# Interactive Help from Python.

# Short for directory of 4 standard available objects.
dir()
print(dir())

# To see the list of builtins objects.
dir(__builtins__)
print(dir(__builtins__))

# To learn about the pow() func.
help(pow)    # This displays the doc of the power function.
# Raise 2 to the power of 10.
print(pow(2, 10))
print("")

# To learn about the hex() func.
hex(10)     # This displays the hexadecimal representation of number 10 in a string.
print(hex(10))
print(0xa)  # To convert a hexadecimal representation back to number.

# To see a list of available modules in Python.
help("modules")     # Note: preferably run this cmd on the Python interactive prompt eg. >>> help("modules")
# To learn about a module and see what objects are available, must first import it.
import math
print(dir())    # If can see the 'math' module at the end of the directory, that means it is ready for use.
print(dir(math))    # To see what is available in the math module.
print(help(math.radians))   # To see help doc on the radians obj from the math module.
print(math.radians(180))    # To printout the value for radians of 180, which is the pi value.





