#!/usr/bin/env python3

# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ

nums = [1, 2, 3, 4, 5]

for num in nums:
	if num == 3:
		print("Found!")
		break
	print(num)

print("")

for num in nums:
	if num == 3:
		print("Found!")
		continue
	print(num)

print("")

for num in nums:
	for letter in "abc":
		print(num, letter)

print("")

for i in range(1, 11):
	print(i)

print("")

x = 0
while True:
	if x == 5:
		break
	print(x)
	x += 1
