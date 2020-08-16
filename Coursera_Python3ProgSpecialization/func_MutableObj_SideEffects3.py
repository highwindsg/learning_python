#!/usr/bin/env python3

"""
To avoid confusing side effects with sharing of mutable objects,
explicitly make a copy of an object and pass the copy in to the
function.
Eg. The built-in list function, which takes a sequence as a
parameter and returns a new list, works to copy an existing list.
Eg. For dictionaries, you can similarly call the dict function,
passing in a dictionary to get a copy of the dictionary back as a
return value.
"""

def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"
    return lst


mylst = ["106", "students", "are", "awesome"]
# Using the built-in list() and parse in mylst, then parse it into
# the changeit(), and finally assign to new var name newlst.
newlst = changeit(list(mylst))
print(mylst)
print(newlst)
print("")
