#!/usr/bin/env python3

# To find all data above the average.

# Import the statistics module as it contains the mean func.
import statistics

# Create a data list with varying of temperatures.
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)     # Calculate the average of the data temperature.
print(avg)
print("")

# Using the filter() func to select the data that is greater than the avg.
# The output will be a filter obj in memory location, which is an iterator over the results.
print(
    (filter
     (lambda x: x > avg, data)
     )
)

# Therefore we can use a list() func as a constructor to create a list of the results
# that is greater than the avg.
print(
    list(
        (filter
         (lambda x: x > avg, data)
         )
    )
)

# Alternatively can also see the list of results lesser than the avg.
print(
    list(
        (filter
         (lambda x: x < avg, data)
         )
    )
)
