#!/usr/bin/env python3

# If the module is from another directory, must mentioned from where you import the module name.
from dir1 import myfunctions
# or a faster way to import from dir1 get the myfunction name.
import dir1.myfunctions
# and if the module name is too long, can shorten it.
import dir1.myfunctions as mf

print(myfunctions.add(2, 3))
print(myfunctions.multiply(10, 3))
print("")
print(dir1.myfunctions.add(2, 3))
print(dir1.myfunctions.multiply(10, 3))
print("")
print(mf.add(2, 3))
print(mf.multiply(10, 3))