#!/usr/bin/env python3

greet = "Hello Bob"
newstr = greet.replace("Bob", "Jane")   # Use the .replace() method on var 'greet' and pass in two params
                                        # of old and new string to be replaced.
print(newstr)

print("")

newstr = greet.replace("o", "X")        # Use the .replace() method on var 'greet' and pass in two params
                                        # of old and new string char to be replaced.
print(newstr)
