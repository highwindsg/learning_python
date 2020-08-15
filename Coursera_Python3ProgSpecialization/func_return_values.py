#!/usr/bin/env python3

def square(x):
    # y = x * x     # This line can be redundant and multiplication
    return x * x    # can be done on the return line.

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

""" How many lines will the following code print? """

def show_me_numbers(list_of_ints):
    print(10)
    print("Next we'll accumulate the sum")
    accum = 0
    for num in list_of_ints:
        accum = accum + num
    return accum
    print("All done with accumulation1")

show_me_numbers([4, 2, 4])

print("")

"""
Write a function called decision that takes a string as input,
and then checks the number of characters.
If it has over 17 characters, return “This is a long string”,
if it is shorter or has 17 characters, return “This is a short
string”.
"""

def decision(str):
    
    words = str.split()
    num_words = len(words)
    if num_words > 17:
        ans = "This is a long string"
    else:
        ans = "This is a short string"
    return ans
        
print(decision("Well hello dolly"))
print(decision("In olden days a glimps of stocking was looked on a something shocking but heaven knows, anything goes"))
print(decision("how do you do sir"))

print("")
