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

list1 = [1, 2, 3, 4, 5]
list2 = []

stack = Stack()
for num in list1:
    stack.push(num)

for i in range(len(stack.items)):
    list2.append(stack.pop())

print(list2)
