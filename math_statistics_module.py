#!/usr/bin/env python3

import math
# Calculate the multiplication power of an integer.
powerOftwo = math.pow(2, 3)
print("The power of 2 is", powerOftwo)

import random
# To randomly output any number from the given range selection.
anyNumber = random.randint(0, 100)
print("The random number is", anyNumber)

print("")

import statistics

nums = [1, 5, 33, 12, 46, 33, 2]
print("The list of numbers are:", nums)

print("")

# mean
# Calculate the average mean of the given numbers.
averageMean = statistics.mean(nums)
print("The average mean of the numbers is:", averageMean)

# median
# Calculate the median of the given numbers.
medianNumber = statistics.median(nums)
print("The median of the numbers is:", medianNumber)

# mode
# Calculate the mode of the given numbers.
modeNumber = statistics.mode(nums)
print("The mode of the numbers is:", modeNumber)

# median_high
# Calculate the median high of the given numbers.
medianhigh = statistics.median_high(nums)
print("The median high value of the numbers is:", medianhigh)

