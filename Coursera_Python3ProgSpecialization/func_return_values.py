#!/usr/bin/env python3

def square(x):
    y = x * x
    return y

toSquare = 10
result = square(toSquare)
""" Using '.format()' method to print out the result with first
param var obj 'toSquare' and second var obj 'result'.
"""
print("The result of {} squared is {}.".format(toSquare, result))

print("")

def weird():
    print("here")   # Therefore func call will only print out the
    return 5        # values of 'here' and '5' and will ignore the
    print("there")  # remaining two lines as the first return
    return 10       # statement will ignore the rest.

x = weird()
print(x)

print("")

def longer_than_five(list_of_names):
    for name in list_of_names:  # Iterate over the list to look at each name.
        if len(name) > 5:   # As soon as you see a name longer than 5 letters,
            return True # then return True.
            # If python executes that return statement, the func is over.
    return False    # So in order to get to this line, you need to
    # iterate over the whole list (from the for loop) and when you did not
    # get the expression evaluated to be True at this point, then it is
    # correct to return False.

list1 = ["Sam", "Tera", "Sal", "Amita"]
list2 = ["Rey", "Ayo", "Lauren", "Natalie"]

print(longer_than_five(list1))
print(longer_than_five(list2))

print("")
