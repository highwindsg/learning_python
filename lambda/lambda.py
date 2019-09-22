#!/usr/bin/env python3

"""
lambda functions in Python are also called anonymous functions because they don't have any names.
Sometime they are also called one-line functions because they can be written in single line of code.
For the three functions below we will try to convert them into a lambda function.
"""

from functools import reduce

# def double(x):
#     return x * 2
# def add(x, y):
#     return x + y
# def product(x, y, z):
#     return x * y * z

# Create the lambda func and assign the result to var 'double'.
double = lambda x : x * 2               # This line will take over line 9 - 10.
add = lambda x, y : x + y               # This line will take over line 11 - 12.
product = lambda x, y, z : x * y * z    # This line will take over line 13 - 14.

# Client call the var in other func, eg. print() func.
print(double(10))       # Print out the result of double func with param 10.
print(add(10, 20))      # Print out the result of add func with two params of 10 and 20.
print(product(10, 20, 30))  # Print out the result of the product func with three params of 10, 20 and 30.

"""
lambda functions are generally used which takes functions as an argument or returns functions as the result.
More example on how to use lambda function with other functions eg. filter, reduce and map.
"""

# filter, reduce and map
my_list = [2, 5, 8, 10, 9, 3]
my_list2 = [1, 4, 7, 8, 5, 1]

# Passing the lambda double func and 'my_list' var as params to the map() func.
# Therefore the lambda func will apply the double func to every item in the list.
# And then assign the result to a var 'a'.
a = map(lambda x : x * 2, my_list)
print(list(a))  # Passing the var 'a' which is the result of the map() func to a list so that it can be printed out.

# Passing the lambda add func and two list params to the map() func.
# This will add the 1st number from 'my_list' with the 1st number from 'my_list2', and so on.
b = map(lambda x, y : x + y, my_list, my_list2)
print(list(b))

# Using the filter() func to filter out the answer.
# This will find out what numbers in the list are divisible by 2 and filter them out as results and return to the func.
c = filter(lambda x : x%2==0, my_list)
print(list(c))

# Using the filter() func to check which numbers are greater than 5 from 'my_list'.
d = filter(lambda x : True if x > 5 else False, my_list)
print(list(d))

# Based on the two args of x and y, the reduce() func will add 2 and 5 is to 7, then add 7 and 8 is to 15,
# then add 15 and 10 is to 25, then add 25 and 9 is to 34, then 34 and 3 is to 37.
e = reduce(lambda x, y : x + y, my_list)
print(e)
