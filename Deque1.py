#!/usr/bin/env python3

"""
A 'deque' (pronounced as deck), also known as a double-ended queue,
is an ordered collection of items similar to the queue.
It has two ends, a front (extreme right) and a rear (extreme left),
and the items remain positioned in the collection.
New items can be added at either the front or the rear.
Likewise, existing items can be removed from either end.
It does not require the LIFO and FIFO orderings that are enforced by
stacks and queues data structures.
"""

# Create a class 'Deque()' that is empty.
class Deque:
    def __init__(self): # Create a func init start with param self.
        self.items = [] # From self, set the items attrib with a empty list.

    def isEmpty(self):  # Create a func isEmpty with param self to check
        return self.items == [] # whether the deque is empty and return/show
                                # a boolean value of either True or False.

    def addFront(self, item):   # Create a func addFront with params self and
        self.items.append(item) # item, and using the .append() method to
                                # add the item param to the front right.
                                # Hence the deque is modified.

    def addRear(self, item):    # Create a func addRear with params self and
        self.items.insert(0, item)  # item, and using the .insert() method
                                    # with params 0 and the item, as 0 is
                                    # the first item from the left.

    def removeFront(self):  # Remove the front item from the deque by
        return self.items.pop() # using the .pop() method, and also return/
                                # show the item that is removed.
                                # Hence the deque is modified.

    def removeRear(self):   # Remove the rear item from the deque by
        return self.items.pop(0)    # using the .pop(0) method as 0 is the
                                    # first item from the left. And it
                                    # also return/show the item that is
                                    # removed. Hence the deque is modified.

    def size(self): # Return/show the number of items in the deque.
        return len(self.items)  # Return/show an integer.


d = Deque() # Set var d to the class Deque.

print(d.isEmpty())  # Use print() to see what is the return boolean value.

d.addRear(4)    # From Deque class use the addRear() method with param 4.
d.addRear("dog")    # From Deque class use the addRear() method with param "dog".
d.addFront("cat")   # From Deque class use the addFront() method with param "cat".
d.addFront(True)    # From Deque class use the addFront() method with param True.

print(d.size()) # Use print() to see what is the return number of items
                # still remaining in the deque.

print(d.isEmpty())  # Use print() to see what is the return boolean value.

d.addRear(8.4)  # From Deque class use the addRear() method with param 8.4.

print(d.removeRear())   # Use print() to see what is the first item that
                        # is being removed from the extreme left.

print(d.removeFront())  # Use print() to see what is the last item that
                        # is being removed from the extreme right.

