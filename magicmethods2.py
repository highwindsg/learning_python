#!/usr/bin/env python3

"""
When you print a Lion object below, Python calls a magic method __repr__
it inherited from Object on it, and prints whatever the __repr__ method
returns. You can override the inherited __repr__ method to change what
prints out.
"""
class Lion:
    def __init__(self, name):
        self.name = name

    # Returns a string containing a printable representaion of an obj.
    def __repr__(self):
        return self.name


lion = Lion("Dilbert")
print(lion)
"""
Because you overrode the __repr__ method inherited from Object and
changed it to return the Lion object's name, when you print a Lion
object, its name -- in this case, Dilbert -- prints instead of some
memory location that the __repr__ method would have returned.
"""
