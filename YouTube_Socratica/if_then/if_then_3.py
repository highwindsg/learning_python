#!/usr/bin/env python3

# Scalene triangle: All sides have different lengths.
# Isosceles triangle: Two sides have the same length.
# Equilateral triangle: All sides are equal.

a = int(input("The length of side 'a' = "))
b = int(input("The length of side 'b' = "))
c = int(input("The length of side 'c' = "))

# Now compare all sides of the triangle.
if a != b and b != c and a != c:
    print("This is a scalene triangle as all three sides are not the same.")
elif a == b and b == c:
    print("This is an equilateral triangle as all three sides are the same.")
else:
    print("This is an isosceles triangle as only two sides are the same.")
