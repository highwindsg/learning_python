#!/usr/bin/env

class Stack:
    def __init__(self):
        self.items = []

#    def is_empty(self):
#        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

#    def peek(self):
#        last = len(self.items)-1
#        return self.items[last]

#    def size(self):
#        return len(self.items)

stack = Stack()
for c in "Hello":   # Iterate through each character in the string
    stack.push(c)   # by using a for_loop and putting each character
                    # in the stack var.

reverse = ""    # Create a var named 'reverse' with a empty string.

# Iterate though the number of items in the stack and,
for i in range(len(stack.items)):
    # take each item off the stack (LIFO) and put it in the reverse
    # var until the for_loop iteration completes.
    reverse += stack.pop()

print(reverse)

""" Note that in the above Stack class, the function methods of
is_empty(), peek() and size() are not actually used for reversing
a string with a Stack. """

