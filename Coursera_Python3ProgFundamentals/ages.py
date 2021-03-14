#!/usr/bin/env python3

age1 = input("How old are you? ")
age2 = input("How old is your best friend? ")

print(int(age1) + int(age2))

# This line below will show a concatenation, not sum.
print(int(age1 + age2))

# This line below will show a concatenation, not sum.
print(str(int(age1 + age2)))

x = int(age1)
y = int(age2)
print(str(x + y))

