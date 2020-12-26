#!/usr/bin/env python3

"""
We can’t modify the elements of a tuple, but we can make a 
variable reference a new tuple holding different information. 
Thankfully we can also use the slice operation on tuples as 
well as strings and lists. To construct the new tuple, we can 
slice parts of the old tuple and join up the bits to make the 
new tuple. So julia has a new recent film, and we might want to 
change her tuple. We can easily slice off the parts we want and 
concatenate them with the new tuple.
"""

julia = ("Julia",
"Roberts",
1967,
"Duplicity",
2009,
"Actress",
"Atlanta, Georgia")

print(julia[2])
print(julia[2:6])
print(len(julia))
julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)
print("")

