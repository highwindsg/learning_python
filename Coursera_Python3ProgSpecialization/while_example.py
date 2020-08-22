#!/usr/bin/env python3

def sumTo(aBound):
    """ Return the sum of 1+2+3 ... n """

    theSum = 0  # Accumulator to keep track of the sum so far.
    aNumber = 1 # Another accumulator to keep track of where we are.
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

print(sumTo(4))
print(sumTo(1000))
print("")


"""
Write a while loop that is initialized at 0 and stops at 15.
If the counter is an even number, append the counter to a list
called eve_nums.
"""

count = 0
eve_nums = []

while count <= 15:
    if count %2 == 0:
        eve_nums.append(count)
    count += 1
print(count)
print(eve_nums)
print("")


"""
Write a function called stop_at_four that iterates through a list
of numbers. Using a while loop, append each number to a new list
until the number 4 appears. The function should return the new
list.
"""

def stop_at_four(list):

    idx = 0
    new_lst = []

    while (idx < len(list)) and (list[idx] != 4):   # True and True = True
        new_lst.append(list[idx])   # Add the number referenced by
                                    # the index from the 'list' into
                                    # the new_lst.
        idx += 1    # Then increase the idx count by 1 to look at
                    # the next number in 'list'.
    return new_lst

# Func call and parse in one param of a list and print out.
print(stop_at_four([3, 7, 5, 9, 9, 0, 4, 3, 2, 5]))
print("")


"""
Below is provided a for loop that sums all the elements in list1.
Write code that accomplishes the same task, but instead use a while
loop. Assign the accumulator variable to the name accum.
"""

list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0 # Assign the accumulator tot with 0 first.
for elem in list1:
    tot = tot + elem
print(tot)
print("")

""" Alternatively, if using while loop """

idx = 0
accum = 0
# print(len(list1))
while idx < len(list1):
    accum = accum + list1[idx]
    idx += 1
print(accum)
print("")

