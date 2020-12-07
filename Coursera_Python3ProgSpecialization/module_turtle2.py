#!/usr/bin/env python3

"""
Modify the program file 'module_turtle.py' so that before it creates
the window, it prompts the user to enter the desired background color.
It should store the user’s responses in a variable, and modify the
color of the window according to the user’s wishes.
(Hint: you can find a list of permitted color names at
https://www.w3schools.com/colors/colors_names.asp. 
It includes some quite unusual ones, like “PeachPuff” and “HotPink”.)

Do similar changes to allow the user, at runtime, to set tess’ color.

Do the same for the width of tess’ pen. Hint: your dialog with the user
will return a string, but tess’ pensize method expects its argument to
be an int. That means you need to convert the string to an int before
you pass it to pensize.

Then finally run the program which draws a rectangle.
"""
