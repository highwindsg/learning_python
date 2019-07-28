#!/usr/bin/env python3

friends = ["Joseph", "Glenn", "Sally"]
print(friends)
print(friends[2])   # Print out the third slice from the friends list (eg. 0, 1, 2)
print("")
friends[2] = "Kenny"    # Replace slice 3 with new string, because a list is mutable, can be changed.
print(friends)
print(friends[2])
print("")
print(len(friends))     # Print out the number of items in the list, regardless of strings or numbers.
