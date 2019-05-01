#!/usr/bin/env python3

"""
Other than lists, tuples and dictionaries, stack is also a data structure.
The 'stack' data structure have five methods.
- is_empty(): returns True if the stack is empty, and False if not empty.
- push(): adds an item to the top of the stack.
- pop(): removes and returns the value of the top item from the stack.
- peek(): returns the value of the top item in the stack, but does not remove it.
- size(): returns an integer representing the number of items in the stack.
"""

class Stack:    # Create a class named Stack.
    def __init__(self): # Create a init start function with param self.
        self.items = [] # From self, set the items attribute with an empty list.

    def is_empty(self): # Create a is_empty method function with param self.
        return self.items == [] # From self, the items attribute is equal or same as
                                # the empty list, and returns the value to the
                                # is_empty() method.

    def push(self, items):  # Create a push method function with params self and items.
        self.items.append(items)    # From self, get the items attribute and append it
                                    # with items.

    def pop(self):  # Create a pop method function with param self.
        return self.items.pop() # From self, get the items attribute and pop the last
                                # item from the list. (eg. LIFO 'last-in-first-out')
                                # and then return the value to the pop() method.

    def peek(self): # Create a peek method function with param self.
        last = len(self.items)-1    # Assign var 'last' with the last item from the list
                                    # by using the len() method on the items list, and -1
                                    # as the reverse index to select the last item in
                                    # the list.
        return self.items[last] # From self, get the items attribute with the 'last' var
                                # and returns the value of that var to the peek() method.

    def size(self): # Create a size method function with param self.
        return len(self.items)  # From self, get the number of items in the list using
                                # the len() method and returns the value (which is the
                                # number of items in the list) to the size() method.


stack = Stack() # Assign the var 'stack' with the class Stack().
print(stack.is_empty()) # Print out the value of is_empty() method by calling the stack
                        # var obj on the is_empty() method.
                        # As there is indeed nothing and empty in var obj 'stack,
                        # is_empty() method will return True.

stack.push(1)   # In the 'stack' var obj, add in a new item by using the push() method
                # and putting the param with int 1.
iprint(stack.is_empty()) # Now print out the value of is_empty() method by calling the
                        # is_empty() method on the stack var obj. As now there is a
                        # int 1 in var obj 'stack', is_empty() method will return False.

item = stack.pop()  # Removes the latest item from the stack by using the pop() method
                    # and returns the value of that removed item to var 'item'.
print(item) # Print out what is the removed item, by calling the print() function method
            # on var 'item'.
print(stack.is_empty()) # Now print out the value of is_empty() method by calling the
                        # is_empty() method on the stack obj var. And as the pop()
                        # function method on line 57 removed the last item, therefore
                        # is_empty() will return True, as the stack is empty again.

# Now finally, take a look at the stack's content and get its size.
for i in range(0, 6):   # Up to index 6 but does not include 6.
    stack.push(i)   # push() method will add onto the stack six times in this for_loop.

print(stack.peek()) # Print out to only see what is the last value on top of the stack.
print(stack.size()) # Print out the integer representing how many items in total are
                    # there actually in the list.

