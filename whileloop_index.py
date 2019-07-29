#!/usr/bin/env python3

# Looping through strings.
fruit = "banana"
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

print("")

# Or use a 'forloop', because the less code you write, the better.
fruit = "banana"

for letter in fruit:
    print(letter)
