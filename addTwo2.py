#!/usr/bin/env python3

# To calculate the total sum by providing a 'startingValue' and add with two.
def addTwo(startingValue):
    totalValue = startingValue + 2
    return totalValue   # Returns a result to the caller

# Call the function twice with different arguments
sum1 = addTwo(5)
sum2 = addTwo(10)

print("The results of adding 2 to 5 and 2 to 10 are:", sum1, "and", sum2)
