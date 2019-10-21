#!/usr/bin/env python3

alphabets = ["A", "B", "C", "D", "E", "F", "G"]
print(alphabets)
print("")

alphabets.append("X")
alphabets.append("Y")
alphabets.append("Z")
print(alphabets)
print("")

print(alphabets[0])
print(alphabets[-1])
print("")

print(alphabets[0:3])
print("")

num = [7, 8, 9, 0]
alpha = ["H", "I", "J", "K"]
num_alpha = num + alpha     # Concatenating two list into one var obj.
print(num_alpha)
