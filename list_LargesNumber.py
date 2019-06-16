#!/usr/bin/env python3

# Find which is the largest number in the list.

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]    # Set the first index assumed to be the largest for now.

for num in numbers:
    if num > max:
        max = num
#    print(max)     # Uncomment this line to see the for loop comparing which
                    # num is larger.
print(max)
