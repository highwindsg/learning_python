#!/usr/bin/env python3

""" To find out how many hours, mins and secs are there in 7684 total secs. """

# Total seconds to calculate.
total_secs = 7684

# To find out how many hours in a sec by using int division //.
hours = total_secs // 3600

# To find out the remaining secs that is not enough to make up an hour by using
# % mod.
secs_still_remaining = total_secs % 3600

# To find out how many more minutes from the seconds remaining by using // mod
# on 60, which is the number of seconds in a minute.
minutes = secs_still_remaining // 60

# Since number of minutes has been found, then finally can find out how may 
# seconds does it finally still left that is not enough to make up a minute by
# using % mod on 60 because 1 min is equal to 60 secs.
secs_finally_remaining = secs_still_remaining % 60


print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)
print("")
