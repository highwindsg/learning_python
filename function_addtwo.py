#/usr/bin/env python3

def addtwo(a, b):
    added = a + b
    return added


a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))
sum = addtwo(a, b)
print(sum)


