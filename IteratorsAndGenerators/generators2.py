#!/usr/bin/env python3

""" So instead of creating the iterator class in 'iterators.py' file where the '__iter__()' and
'__next__()' functions are explicitly defined with the raise exception, we can shorten the program
by using the 'yield' generator keyword in a for loop.
"""

def list_iterator(list):    # Define a func named 'list_iterator()' with param 'list'.
    for i in list:          # In the for loop we get the value of 'i' in the 'list' from
        yield i             # the 'yield' keyword.

a = [1, 2, 3, 6, 5, 4]      # Create a list of numbers and assign to var 'a'.
mylist = list_iterator(a)   # Pass the var obj 'a' to the 'list_iterator()' func and assign to var 'mylist'.

print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))     # This will cause a StopIteration error automatically as it exceeds the list.
