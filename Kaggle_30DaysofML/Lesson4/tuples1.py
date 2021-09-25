#!/usr/bin/env python3

# Tuples, uses parentheses () instead of sqaure brackets [].

t = (1, 2, 3)
print(t)
print("")


# Cannot be modified, immutable.
#t[2] = 4
#print(t)
#print("")


# Tuples used for functions that have multiple return values.
x = 0.125

print(
    x.as_integer_ratio()
)
print("")


# Multiple return values can be individually assigned.
numerator, denominator = x.as_integer_ratio()
print(numerator, denominator)
print("")


# Swapping two variables values.
a = 1
b = 0
a, b = b , a
print(a, b)
print("")
