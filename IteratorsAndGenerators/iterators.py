#!/usr/bin/env python3

""" About the '__iter__()' and '__next__()' function.
The above two functions are similar to a loop when running an iteration.
"""

class ListIterator:

    def __init__(self, list):   # Define a init start func with params 'self' and 'list'.
        self.__list = list      # From self, set a private '.__list' attrib and assign to var obj 'list'.
        self.__index = -1       # From self, set a private '.__index' attrib and assign to a value of '-1'.

    def __iter__(self):     # Define a '__iter__()' func with 'self' param.
        return self         # Return the value of 'self' to the func.

    def __next__(self):     # Define a '__next__()' func with 'self' param.
        self.__index += 1   # As similar to a loop, increase the private '.__index' by 1. (eg. i = i + 1)
        if self.__index == len(self.__list):    # As soon as the value of the index is the same as the list,
            raise StopIteration                 # then raise a exception call of 'StopIteration'.
        return self.__list[self.__index]    # From 'self', get the private var of '.__index' from '.__list',
                                            # and return the value to the '__next__()' func.


a = [1, 2, 3, 6, 5, 4]      # Create a list of numbers and assign to var obj 'a'.
mylist = ListIterator(a)    # Client call the 'ListIterator' class and pass in the param obj 'a'.
it = iter(mylist)       # Use the 'iter()' func, pass in the var 'mylist' and assign it var 'it'.


print(next(it))     # Client call the 'next()' method and pass in the var 'it' that will printout the next
                    # increased value.
print(next(it))     # Client call again the 'next()' method to printout the next increased value.
print(next(it))     # Again client call the 'next()' method to printout yet the next increased value.
print(next(it))     # Again client call ...
print(next(it))     # Again client call ...
print(next(it))     # Again client call the last number.
print(next(it))     # This extra client call will have error as it is out of range of list 'a'.
