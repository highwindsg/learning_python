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

""" The class Data has an instance variable called 'nums' that contains a list of integers.
Once you create a Data object, there are two ways you can change the items in 'nums'.
"""

""" You can change the items in 'nums' by directly accessing the 'nums' instance variable:,
"""
data_one = Data()       # Assign var 'data_one' to class Data().
data_one.nums[0] = 100  # From var 'data_one', get the instance variable of 'nums' list at the
                        # first index and assign to 100.
print(data_one.nums)

"""
or by using the 'change_data' method:
"""
data_two = Data()       # Assign var 'data_two' to class Data().
data_two.change_data(0, 100)    # From var 'data_two', get the instance variable of
                                # 'change_data' and with params 0 and 100.
print(data_two.nums)

""" Note that if the above 'nums' list is changed to a tuple instead of a list, then the
code will not work because tuples are immutable , means cannot be changed.
"""
