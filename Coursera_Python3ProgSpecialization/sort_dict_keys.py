#!/usr/bin/env python3

# Sorting a dictionary's keys.

L = ["E", "F", "B", "A", "D", "I", "I", "C", "B", "A", "D", "D", "E"]

d = {}  # Create a empty dict accumulator first.
for x in L:
    if x in d:
        d[x] = d[x] + 1 # If item is inside dict already, then set counter
                        # to increase by 1.
    else:
        d[x] = 1    # But if the item is not inside dict yet, then
                    # initialize counter to start of with 1 first.

print(d)

# Sorting the keys in alphabetical order by using the sorted() func,
# by parsing in d.keys() as a param into the sorted() func.
for x in sorted(d.keys()):
    print("{} appears in {} times".format(x, d[x]))
print("")

# Sorting by the number of counts the letter appears from lease to
# most frequent. Parse into the sorted() func a second optional param
# key with a lambda func to get the value of that key in the dict.
# The property of key k that is supposed to be returned is its associated
# value in the dictionary.
# More explanation for line 35:
# The function sorted is invoked. Its first parameter value is a
# dictionary, which really means the keys of the dictionary. The
# second parameter, the key function, decorates the dictionary key
# with a post-it note containing that key’s value in dictionary d.
# The last parameter, True, says to sort in reverse order.
for x in sorted(d.keys(), key=lambda k: d[k]):
    print("{} appears {} times".format(x, d[x]))
print("")

# Sorting the number of counts the letter appears from most to frequent.
# Parse in a third optional param of reverse=True.
for x in sorted(d.keys(), key=lambda k: d[k], reverse=True):
    print("{} appears {} times".format(x, d[x]))
print("")

# If do not want to use lambda func, can also use a named func.
def g(k):   # Create a func named g() with param k.
    return d[k] # Return the value of k which is the key in the dict.

y = sorted(d.keys(), key=g, reverse=True)

for k in y:
    print("{} appears {} times".format(k, d[k]))
print("")



"""
Sort the following dictionary based on the keys so that they are
sorted a to z. Assign the resulting value to the variable sorted_keys.
"""

dictionary = {
    'Flowers': 10, 
    'Trees': 20, 
    'Chairs': 6, 
    'Firepit': 1, 
    'Grill': 2, 
    'Lights': 14
    }

sorted_keys = sorted(dictionary.keys())
print(sorted_keys)
print("")


"""
Below, we have provided the dictionary groceries, whose keys are
grocery items, and values are the number of each item that you need
to buy at the store. Sort the dictionary’s keys into alphabetical
order, and save them as a list called grocery_keys_sorted.
"""

groceries = {
    'apples': 5, 
    'pasta': 3, 
    'carrots': 12, 
    'orange juice': 2, 
    'bananas': 8, 
    'popcorn': 1, 
    'salsa': 3, 
    'cereal': 4, 
    'coffee': 5, 
    'granola bars': 15, 
    'onions': 7, 
    'rice': 1, 
    'peanut butter': 2, 
    'spinach': 9
    }

grocery_keys_sorted = sorted(groceries.keys())
print(grocery_keys_sorted)
print("")


"""
Sort the following dictionary’s keys based on the value from highest
to lowest. Assign the resulting value to the variable sorted_values.
"""

dictionary = {
    'Flowers': 10, 
    'Trees': 20, 
    'Chairs': 6, 
    'Firepit': 1, 
    'Grill': 2, 
    'Lights': 14
    }

sorted_values = sorted(dictionary.keys(), key=lambda k: dictionary[k], reverse=True)
print(sorted_values)
print("")

