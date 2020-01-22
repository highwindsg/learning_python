#!/usr/bin/env python3

# https://www.youtube.com/watch?v=CqvZ3vGoGs0

import my_module as mm
# Or
from my_module import find_index, test
import sys
import random
import math
import datetime
import calendar
import os
# import antigravity    # The import of antigravity will cause the program to run a webbrowser to load to a site.

courses = ["History", "Math", "Physics", "CompSci"]

# Func call find_index() and pass in the params of var courses and a subject, then assign it to var index.
index = find_index(courses, "Math")
print(index)
print(test)
print("")

# The printout below from sys.path will show where the imports comes from. Path order from first to the last.
print(sys.path)
print("")

# From the random module, use the choice method and pass in the param courses, then assign to var random_course.
random_course = random.choice(courses)
print(random_course)    # This will print out a course randomly.
print("")

# From the math module, use the radians method to convert a number to a radian value.
rads = math.radians(90)
print(rads)     # This will print out the radian converted value.
print(math.sin(rads))       # This will print out the sin value of the radian convered value.
print("")

# From the datetime module, use the date.today() method and assign to var today.
today = datetime.date.today()
print(today)    # This will print out the current day's value in YYYY-MM-DD format.
print("")

# From the calendar module, use the isleap() method and pass in a param of year 2017.
print(calendar.isleap(2017))    # This will print out if 2017 is a leap year or not, in True or False.

# From the os module, use the getcwd() method of get working directory, and print out the current working directory.
print(os.getcwd())
print("")

# This will print out the dunder file of the os module, which is the python script of the os module.
print(os.__file__)
