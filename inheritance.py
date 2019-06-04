#!/usr/bin/env python3

# The files inheritanceChef.py, inheritanceChineseChef.py and inheritance.py
# are in the same working dir.

from inheritanceChef import Chef
from inheritanceChineseChef import ChineseChef

# Set var 'myChef' to an instance of class chef().
myChef = Chef()
myChef.make_special_dish()  # Client call the var myChef and get the attrib
                            # of .make_special_dish() function.

# Set var 'myChineseChef' to an instance of class ChineseChef().
myChineseChef = ChineseChef()
myChineseChef.make_fried_rice() # Client call the var myChineseChef and get
                                # the attrib of .make_fried_rice() function.
