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

