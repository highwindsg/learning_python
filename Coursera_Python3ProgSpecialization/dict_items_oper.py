#!/usr/bin/env python3

mydict = {"cat": 12, "dog": 6, "elephant": 23}
print(mydict)
print("")

# Adding the values of two key values to a new item.
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict["mouse"])
print(mydict)
print("")

# To add 5 to the number of elephant.
# Always use the existing key value and then add with new value.
mydict["elephant"] = mydict["elephant"] + 5
print(mydict)
print("")

# Use sum() func to calculate the total sum of all values in a dict.
# First use the .values() method to return values of a dict.
values = mydict.values()    # Use the .values() method on 'mydict' dict
                            # and assign to var 'values'.
total = sum(values) # Use the sum() func with 'values' as param and
                    # assign the sum values to var 'total'.
print(total)
print("")

# Calculate the division of values from key items in a dict.
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
answer = mydict.get("cat") // mydict.get("dog")
print(answer)
print("dog" in mydict)  # Boolean answer true or false if 'dog' is in dict.
print("")

# Given the dictionary swimmers, add an additional key-value pair to 
# the dictionary with "Phelps" as the key and the integer 23 as the 
# value. 

swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}
swimmers["Phelps"] = 23
print(swimmers)
print("")
