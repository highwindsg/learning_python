#!/usr/bin/env python3

def f(x):
    return x + 1

num = int(input("Enter a integer number: "))

z = f(num)
print(z)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")
