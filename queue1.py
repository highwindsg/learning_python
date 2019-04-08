#!/usr/bin/env python3

"""
Queue is another data structure. But unlike a stack, a queue is a
firstin-firstout (FIFO) whereby first item added is also first to be
taken out.
- enqueue():    read as entry to a queue line (firstin).
- dequeue():    read as to delist from a queue line (firstout).
- is_empty():   checks and returns True if the queue line is empty, or
                returns False if otherwise.
- size():       returns the number of items in the queue line.
"""

class Queue:
    def __init__(self): # Create a init start function with param self.
        self.items = [] # From self, get the items attribute and set to a
                        # empty list for now.

    def is_empty(self): # Create a is_empty function method with param self.
        return self.items == [] # From self, set items attribute is equal to a
                                # empty list for now and return it to the
                                # is_empty function.

    # Create a function method named enqueue (entry) with param self and items.
    def enqueue(self, items):
        # From self, get the items attribute and use the insert method to put
        # the value as the first one in line.
        self.items.insert(0, items)

    # Create a function method named dequeue (to delist) with param self.
    def dequeue(self):
        # From self, get the attribute values from the items list and use the
        # pop method to delist the first one in line (FIFO).
        return self.items.pop()

    def size(self): # Create a function method named size.
        return len(self.items)  # Return the number of items to the size function
                                # method by using the len method on the items list.


a_queue = Queue()   # Set var 'a_queue' to class Queue.
print(a_queue.is_empty())   # Print out the value of var 'a_queue' by calling
                            # the is_empty() method on var obj 'a_queue'.
                            # As there is indeed nothing and empty in var obj
                            # 'a_queue', is_empty() will return True.

