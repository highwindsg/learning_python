#!/usr/bin/env python3

L1 = [1, 7, 4, -2, 3]
L2 = ["Cherry", "Apple", "Blueberry"]


L1.sort()
print(L1)

print("----")

L2.sort()
print(L2)

print("")


""" Using sorted(obj) as a function, rather than a method and return
the sorted obj as a new list. This way the original obj will not be
changed. """

L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2)   # Unchanged.

print("----")

L2.sort()
print(L2)
print(L2.sort())    # Return value is None.

print("----")

print(sorted("Apple"))  # The string will be arranged in alphabetical
                        # order in a list.
print("")
