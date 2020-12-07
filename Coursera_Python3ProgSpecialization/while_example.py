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

count = 0   # Initialize counter to start at zero first.
eve_nums = []   # Initialize an empty list first.

while count <= 15:
    if count %2 == 0:
        eve_nums.append(count)
    count += 1
print(count)
print("The list of even numbers count are:", eve_nums)
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
Write a function, sublist, that takes in a list of numbers as the
parameter. In the function, use a while loop to return a sublist
of the input list. The sublist should contain the same values of
the original list up until it reaches the number 5 (it should not
contain the number 5).
"""

def sublist(list):
    
    idx = 0
    new_lst = []
    
    while (idx < len(list)) and (list[idx] != 5):
        new_lst.append(list[idx])
        idx += 1
    return new_lst

print(sublist([1, 2, 3, 4, 5, 6, 7, 8]))
print("")



"""
Write a function called check_nums that takes a list as its
parameter, and contains a while loop that only stops once the
element of the list is the number 7. What is returned is a list
of all of the numbers up until it reaches 7.
"""

def check_nums(list):
    
    idx = 0
    new_lst = []
    
    while (idx < len(list)) and (list[idx] != 7):
        new_lst.append(list[idx])
        idx += 1
    return new_lst

print(check_nums([1, 2, 3, 4, 5, 6, 7, 8]))
print("")



"""
Write a function, sublist, that takes in a list of strings as the
parameter. In the function, use a while loop to return a sublist
of the input list. The sublist should contain the same values of
the original list up until it reaches the string “STOP” (it should
not contain the string “STOP”).
"""

def sub_list(str):
    
    idx = 0
    new_str_lst = []
    
    while (idx < len(str)) and (str[idx] != "STOP"):
        new_str_lst.append(str[idx])
        idx += 1
    return new_str_lst

print(sub_list(["One", "Two", "Three", "STOP", "Go"]))
print("")



"""
Write a function called stop_at_z that iterates through a list of
strings. Using a while loop, append each string to a new list
until the string that appears is “z”. The function should return
the new list.
"""

def stop_at_z(str):

    idx = 0
    new_str_lst = []
    
    while (idx < len(str)) and (str[idx] != "z"):
        new_str_lst.append(str[idx])
        idx += 1
    return new_str_lst

print(stop_at_z(['c', 'b', 'd', 'z', 'zebra', 'z', 'h', 'r']))
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
print(len(list1))
while idx < len(list1):
    accum = accum + list1[idx]
    idx += 1
print(accum)
print("")



"""
Below is a for loop that works. Underneath the for loop, rewrite
the problem so that it does the same thing, but using a while
loop instead of a for loop. Assign the accumulated total in the
while loop code to the variable sum2. Once complete, sum2 should
equal sum1.
"""

lst = [65, 78, 21, 33]
sum1 = 0

for x in lst:
    sum1 = sum1 + x

print(sum1)

# Alternatively, using while loop to calculate sum2.

sum2 = 0
idx = 0

print(len(lst))
while idx < len(lst):
    sum2 = sum2 + lst[idx]
    idx += 1
    
print(sum2)
print("")



"""
Challenge:
Write a function called beginning that takes a list as input and
contains a while loop that only stops once the element of the
list is the string ‘bye’. What is returned is a list that contains
up to the first 10 strings, regardless of where the loop stops.
(i.e., if it stops on the 32nd element, the first 10 are returned.
If “bye” is the 5th element, the first 4 are returned.) If you want
to make this even more of a challenge, do this without slicing.
"""

def beginning(list):

    idx = 0
    new_str_lst = []

    while (idx < len(list)) and (list[idx] != "bye"):
        new_str_lst.append(list[idx])
        idx += 1
        # print(new_str_lst)
        if len(new_str_lst) >= 10:
            break
    return new_str_lst


print(beginning(["One", "Two", "Three", "STOP", "bye", "Go"]))
print(beginning([
                'hello',
                'hi',
                'hiyah',
                'howdy',
                'what up',
                'whats good',
                'holla',
                'good afternoon',
                'good morning',
                'sup',
                'see yah',
                'toodel loo',
                'night',
                'until later',
                'peace',
                'bye',
                'good-bye',
                'g night'
                ])
                )
print("")

