#!/usr/bin/env python3

course = "Python for Beginners"
print(course[0])    # Prints out the first index of what's inside the course var.
print(course[-2])   # Prints out the third index from the last where 'P' is 0,
                    # 's' is -1 and 'r' is -2.
print(course[0:3])  # Prints out from index 0 up to index 3 but does not include
                    # the index 3.
print(course[0:])   # Prints from index 0 and all the way to the end.
print(course[1:])   # Prints from index 1 and all the way to the end.
print(course[:5])   # Even with no starting index, python will assume starting
                    # from index 0, and prints till index 5 but does not include 5.
print(course[:])    # If no starting and no ending index, python will print out
                    # whole content of the var string.

name = "Jennifer"
print(name[1:-1])   # Prints from 'e' to 'e'.

