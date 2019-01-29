#!/usr/bin/env python3

def f(x, y, z):
    return x + y + z

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

result = f(x, y, z)
print("Sum of the above three numbers is:", result)
