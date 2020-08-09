#!/usr/bin/env python3

# Define a func named 'add_list' with param (alist).
def add_list(alist):
    total = 0   # Initialize counter 'total' to 0 first.
    for num in alist:   # For every 'num' in 'alist',
        total += num    # add the number to the 'total' counter.
    return total    # Parse the value of 'total' by returning it
                    # back to the func name.


my_list = [7, 3, 5, 4]
sum_of_list = add_list(my_list) # Func call 'add_list' and parse in
                                # 'my_list' as param.
print(sum_of_list)

print("")

