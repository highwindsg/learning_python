#!/usr/bin/env python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1]) # After selecting the first index list, then print out
                    # the second index item which is 2.
matrix[0][1] = 20   # Giving a new value of 20 to the matrix.
print(matrix[0][1]) # And then printing out the new value.
print("")

# To print out all the numbers using a nested for loop.
for row in matrix:
    for item in row:
        print(item)

