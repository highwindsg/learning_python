#!/usr/bin/env python3

"""
Write a program that will compute the area of a circle. 
Prompt the user to enter the radius and save it to avariable called 
radius. Print a nice message back to the user with the answer.
Formula: A = πr²
or
Formula: Area of a circle = pi * (radius * radius)
"""

radius = int(input("Enter the radius: "))
pi = 3.14
A = pi * (radius * radius)

print("Area of a circle is", A)
print("")


"""
Write a program that will compute the area of a rectangle. 
Prompt the user to enter the width and height of the rectangle and 
store the values in variables called width and height. Print a nice 
message with the answer.
"""

width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
A = width * height

print("Area of the rectangle is", A)
print("")
