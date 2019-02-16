#!/usr/bin/env python3

# Instead of iterating through tv, you passed tv to 'enumerate' and
# iterated through the result, which allowed you to add a new var 'i'
# that keeps track of the current index.

tv = [
"GOT",
"Narcos",
"Vice"
]

for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)

