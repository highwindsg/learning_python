#!/usr/bin/env python3

L1 = [1, 7, 4, -2, 3]

def absolute(x):
    if x <= 0:
        return x
    else:
        return -x


L2 = sorted(L1, key = absolute)
print(L2)
print("")

# or in reverse order using 'key = absolute' as 1 is absolutely > -2.
# absolute() as a func is therefore parsed into the sorted() func
# as a key param.
print(sorted(L1, reverse = True, key = absolute))
print("")

# or using a lambda expression to represent the absolute func.
L2 = sorted(L1, reverse = True, key = lambda x: absolute(x))
print(L2)
print("")
