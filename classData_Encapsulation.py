#!/usr/bin/env python3

""" The second concept of encapsulation refers to hiding a class's internal data to prevent
the client (the code outside that uses the object) from directly accessing it:
"""
class Data():  # Create a class named Data()'.
    def __init__(self):   # Define a init start function method with params self.
        self.nums = [1, 2, 3, 4, 5]  # From 'self', get the attribute of 'nums' and assign to a
                                     # list of integers.

    # Define a 'change_data' function method with params self, index and n.
    def change_data(self, index, n):
        self.nums[index] = n    # From self, get the instance var of 'nums' with indexing and
                                # assign to 'n'.

""" The class Data has an instance var called 'nums' that contains a list of integers.
Once you create a Data object, there are two ways you can change the items in 'nums'.
"""
