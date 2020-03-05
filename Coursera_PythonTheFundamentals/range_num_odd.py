#!/usr/bin/env python3

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

print(len(s))
print("")

# Print all the numbers in the length of the string 's', the entire
# range.
for i in range(len(s)):
    print(i)
print("")

# Print odd numbers only.
for i in range(1, len(s), 2):   # From range 1, the length of 's' and step 2)
    print(i)
print("")

# Print only even numbers till 10.
for i in range(2, 11, 2):   # From range 1, the length of 's' and step 2)
    print(i)
print("")


# Print every third character in param string 's', starting from the first
# character.
def print_every_third_char(s):
    for i in range(0, len(s), 3):
        print(s[i:i + 1])


print_every_third_char("abcABCabcABC")

