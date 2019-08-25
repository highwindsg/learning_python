#!/usr/bin/env python3

a = [0, 1, 2, 3, 4, 5]
for x in a:
    if x == 2:
        #break   # So once x is equal to 3, then 'break' will come out of the loop.
        continue    # If 'continue' is called, then the codes in the 'if' suite will not be executed.
    print(x)
print("")


i = 0
while i < 5:
    if i == 4:
        #break   # So once i is equal to 3, then 'break' will come out of the loop.
        continue    # If 'continue' is called, then the codes in the 'if' suite will not be executed.
    print(i)
    i += 1
