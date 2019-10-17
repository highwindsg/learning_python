#!/usr/bin/env python3

"""What happens if you open a file that does not exist? Use the 'try' and 'except' method
to raise exception for the type of error, and assign some value to the 'text' var for a
suitable output.
But if the correct file exist, then the program will execute well and print out the content
in var obj 'text'."""

try:
    with open("///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/guido_bio2.txt") as f:
        text = f.read()
except FileNotFoundError:
    text = None

print(text)
