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

# The datetime module contains a class named timedelta, which allows to add or minus number of days from a date.
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
print("")

# SpaceX reused first stage rocket on March 30, 2017 22:27 UTC.

# From datetime module, use the date() class and pass in the params of yyyy, m, dd and assign to var 'launch_date'.
launch_date = datetime.date(2017, 3, 30)
# From the datetime module, use the time() class and pass in the params of hh, min, sec and assign to var 'launch_time'.
launch_time = datetime.time(22, 27, 0)
# From the datetime module, use the datetime() class and pass in the params of yyyy, m, dd, hh, min, sec to var
# 'launch_datetime'.
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print("")

# Print out the launch date, time and date-time together.
print(launch_date)
print(launch_time)
print(launch_datetime)
print("")


# Can also just obtain the individual hour, minutes or seconds from the 'launch_time' var.
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)
print("")

# Can also just obtain the individual year, month or date from the 'launch_date' var.
print(launch_date.year)
print(launch_date.month)
print(launch_date.day)
print("")

# Since the full date and time has been passed into var 'launch_datetime', you can also obtain the individual
# year, month, date, hour, min and secs one at a time.
print(launch_datetime.year)
print(launch_datetime.month)
print(launch_datetime.day)
print(launch_datetime.hour)
print(launch_datetime.minute)
print(launch_datetime.second)
print("")

# Accessing the current date and time from the datetime module and datetime() class, using the today() method.
now = datetime.datetime.today()
print(now)  # This will also print out the current date and time with the last microseconds.
print(now.microsecond)
print("")

# Converting strings value to datetime format, using the datetime module and datetime() class and the strptime() method.
# The 'strptime()' method means to 'strings parse time'. Is used to parse both dates and times.
moon_landing = "7/20/1969"

# From datetime module, get the datetime() class, use the 'strptime()' method and parse in the params of var obj
# 'mood_landing' and the assigned value in month, date and year format.
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)    # This will print out a standard datetime format as an obj, not a string.
print(type(moon_landing_datetime))  # The output will indeed show an instance of datetime class in a datetime module.


