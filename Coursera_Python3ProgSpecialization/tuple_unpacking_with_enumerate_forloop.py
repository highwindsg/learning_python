#!/usr/bin/env python3

"""
The pythonic way to consume the results of enumerate, is to unpack
the tuples while iterating through them, so that the code is easier
to understand.
"""

fruits = ["apple", "pear", "approcot", "cherry", "peach"]
print(fruits)
print("")

for idx, fruit in enumerate(fruits):
    print(idx, fruit)
print("")

# Or to enumerate and unpack into tuples:
for fruit in enumerate(fruits):
    print(fruit)
print("")



"""
Assign the value of the 23rd element of l to the variable checking.
"""

l = ("hi", 
     "goodbye", 
     "python", 
     "106", 
     "506", 
     91, 
     ['all', 'Paul', 'Jackie', "UMSI", 1, "Stephen", 4.5], 
     109, 
     "chair", 
     "pizza", 
     "wolverine", 
     2017, 
     3.92, 
     1817, 
     "account", 
     "readings", 
     "papers", 
     12, 
     "facebook", 
     "twitter", 
     193.2, 
     "snapchat", 
     "leaders and the best", 
     "social", 
     "1986", 
     9, 
     29, 
     "holiday", 
     ["women", "olympics", "gold", "rio", 21, "2016", "men"], 
     "26trombones")

lst = list(l)   # Converting the tuple 'l' into a list 'lst'.
checking = lst[22]
print(checking)
print("")



"""
Assign the value of the last chacter of lst to the variable output. Do this so that the length of lst doesn’t matter.
"""

lst = "Every chess or checkers game begins from the same position and has a finite number of moves that can be played. While the number of possible scenarios and moves is quite large, it is still possible for computers to calculate that number and even be programmed to respond well against a human player..."

output = lst[-1]
print(output)
print("")
