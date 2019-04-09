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

    def size(self): # Create a function method named size with param self.
        return len(self.items)  # Return the number of items to the size function
                                # method by using the len method on the items list.


a_queue = Queue()   # Set var 'a_queue' to class Queue.
print(a_queue.is_empty())   # Print out the value of var 'a_queue' by calling
                            # the is_empty() method on var obj 'a_queue'.
                            # As there is indeed nothing and empty in var obj
                            # 'a_queue' for now, is_empty() will return True.

print() # Prints a empty line.

# Add items and check the queue's size.
for i in range(5):  # Iterate from range 0 up to 5 but does not include 5.
    a_queue.enqueue(i)  # For a_queue, use the enqueue() method on it and pass
                        # in the param of int i.
print(a_queue.size())   # Call the print function on var a_queue and use the
                        # size() method to return the number of items in the
                        # queue line. Number of items in queue line will be 5.

print() # Prints a empty line.

# Remove each item from the queue.
for i in range(5):  # Iterate from range 0 up to 5 but does not include 5.
    print(a_queue.dequeue())    # Call the print function on a_queue and use
                                # the dequeue() method to delist items on it.
                                # Print output will show item removed one by one
                                # starting from 0 to 4 (FIFO).

print() # Prints a empty line.

print(a_queue.size())   # Calling the print() function on a_queue and use the
                        # size() method to return the number of items in the
                        # queue line. Number now is 0 as it has been delisted.

print(a_queue.is_empty())   # is_empty() method on a_queue will also be True
                            # as the var a_queue is empty again.
