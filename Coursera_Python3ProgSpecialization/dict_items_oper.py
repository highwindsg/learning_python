#!/usr/bin/env python3

mydict = {"cat": 12, "dog": 6, "elephant": 23}
print(mydict)

# Adding the values of two key values to a new item.
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict["mouse"])
print(mydict)

# To add 5 to the number of elephant.
# Always use the existing key value and then add with new value.
mydict["elephant"] = mydict["elephant"] + 5
print(mydict)

# Use sum() func to calculate the total sum of all values in a dict.
# First use the .values() method to return values of a dict.
values = mydict.values()    # Use the .values() method on 'mydict' dict
                            # and assign to var 'values'.
total = sum(values) # Use the sum() func with 'values' as param and
                    # assign the sum values to var 'total'.
print(total)
