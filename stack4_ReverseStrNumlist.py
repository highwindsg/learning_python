#!/usr/bin/env python3

# Reverse the following list of numbers [1, 2, 3, 4, 5] using a stack.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
for i in "12345":
    stack.push(i)

reverse = []

for i in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)
