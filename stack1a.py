#!/usr/bin/env python3

"""
We can implement the stack using a list where the top is at the beginning
instead of at the end. In this case, the pop() and append() method would
have the index position 0 (the first item in the list) explicitly.
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

"""
The ability to change the physical implementation of an abstract data type
while maintaining the logical characteristics is an example of abstraction
at work.
"""

s = Stack()
print(s.isEmpty())
print("")

s.push(4)
s.push("dog")
print(s.peek())
print("")

s.push(True)
print(s.size())
print("")

print(s.isEmpty())
print("")

s.push(8.4)
print(s.pop())
print("")

print(s.pop())
print("")

print(s.size())

