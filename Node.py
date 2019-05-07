#!/usr/bin/env python3

"""
The basic building block for an unordered linked list implementation
is the node.
Each node object must hold at least two pieces of information.
First, the node must contain the list item itself.
We will call this the data field of the node.
In addition, each node must hold a reference to the next node.
"""

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


temp = Node(93)
print(temp.getData())

