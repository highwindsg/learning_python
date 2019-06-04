#!/usr/bin/env python3

# The files inheritanceChef.py, inheritanceChineseChef.py and inheritance.py
# are in the same working dir.

from inheritanceChef import Chef

# Inside of this class ChineseChef, I want to be able to use all the functions
# of the Chef class.
class ChineseChef(Chef):    # Rather than copying the other three funcs in, we
                            # parse in the param of Chef. So now the class
                            # ChineseChef will inherit the other three funcs
                            # from the Chef class from module inheritanceChef.

    def make_fried_rice(self):
        print("The chef makes fried rice")
