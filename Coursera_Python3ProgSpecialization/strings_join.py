#!/usr/bin/env python3

"""
The opposite of .split() medthod is the .join() method.
"""

wds = ["red", "blue", "green"]
glue = ";"
s = glue.join(wds)
print(s)
print(wds)
print("")

print("***".join(wds))
print("".join(wds))
print("")


"""
Write code that combines the following variables so that the sentence “You are 
doing a great job, keep it up!” is assigned to the variable message. Do not edit 
the values assigned to by, az, io, or qy.
"""

by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

message = by + " " + az + io + ", " + qy
print(message)
print("")


"""
What is the type of a?
"""

b = "My, what a lovely day"
x = b.split(',')    # 'b' is split into a list and assigned to var 'x'
z = "".join(x)  # then 'x' is joined back into str and assigned to var 'z'
y = z.split()   # then 'z' is split into a list again and assigned to var 'y'
a = "".join(y)  # and finally 'y' list is joined back again and assigned to var 'a'.

print(type(a))
print("")
