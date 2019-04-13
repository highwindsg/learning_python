#!/usr/bin/env python3

""" If you search through a list of numbers and found the number,
you stop. And if you search through the entire list without
finding the number, you also stop, because the number isn't there.
"""

# Define a function named 'ss' with params 'number_list' and 'n'.
# Read ss as sequential search.
def ss(number_list, n):
    found = False   # Firstly, set the var found and assign to False
                    # to indicate number not found yet.
    # Use a for_loop and iterate through the number_list and check
    # if it is in that number_list.
    for i in number_list:
        if i == n:  # If the number in iteration is the same as 'n',
            found = True    # then set var 'found' to True and
            break   # stop the loop.
    return found    # And then return the value of var 'found' to
                    # the ss() function.


# Assign the var numbers with a range of numbers.
numbers = range(0, 100)
# Call the ss() function with params of var numbers and a 2,
# and assign to var s1.
s1 = ss(numbers, 2)
print(s1, "as number 2 is found within the range.")
# Call the ss() function with params of var numbers and a 202,
# and assign to var s2.
s2 = ss(numbers, 202)
print(s2, "as number 202 is not found within the range.")
