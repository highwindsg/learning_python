#!/usr/bin/env python3

#You can store containers in other containers.
#For example, you can store lists in a list.

lists = []

rap = ["Kanye West",
       "Jay Z",
       "Eminem",
       "Nas"
       ]

rock = ["Bob Dylan",
        "The Beatles",
        "Led Zeppelin"
        ]

djs = ["Zeds Dead",
       "Tiesto"
       ]

# Below will store the three lists of rappers, rockers and DJs into the first
# empty 'lists'.
lists.append(rap)
lists.append(rock)
lists.append(djs)

# Therefore the 'lists' now has three indexes and each index is a list itself.
print(lists)
print("")

# Only print out the rappers list and adding another new rapper to it.
rap = lists[0]
rap.append("Kendrick Lamar")
print(rap)
print(lists)

