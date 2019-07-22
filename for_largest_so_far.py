#!/usr/bin/env python3

largest_so_far = -1

# Print out two columns, first with the number before, and second with the largest so far number.
print("Before", largest_so_far)

for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)  # Print out the two columns of the new largest so far and the next number.

print("After", largest_so_far)
