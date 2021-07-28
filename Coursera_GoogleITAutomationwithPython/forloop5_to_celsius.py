#!/usr/bin/env python3

def to_celsius(x):
    return (x-32) * 5/9

for x in range(0, 101, 10): # range starts from 0 to 101 so as to stop at 100, at a jump of 10 each.
    print(x, to_celsius(x))
    
print("")
