#!/usr/bin/env python3

import datetime

# To see the directory of the datetime module.
print(dir(datetime))

# To see the help doc of the objects available from the datetime module in Python interactive mode.
print(help(datetime.date))

# To set a birthdate for the founder of Python eg. Guido van Rossum.
gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

# The datetime module contains a class named timedelta, whoch allows to add or minus number of days from a date.
mill = datetime.date(2000, 1, 1)    # To set 2000-01-01 to var 'mill' for millennial .
print(mill)
dt = datetime.timedelta(100)
""" From datetime module, get the timedelta class attrib and pass in param positive
value of 100 to increase the days, or a negative value will reduce the days."""
print(mill + dt)    # This print out of mill + dt, will see that the datetime changes as 100 days are added to mill.

# Python default date is yyyy-mm-dd. Can change by using different date format.
# Day-name, Month-name, Day-#, Year
print(gvr.strftime("%A, %B %d, %Y"))
message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))  # Print out the 'message' var in .format() method and pass in the datetime obj of 'gvr'.

