#!/usr/bin/env python3

# https://www.youtube.com/watch?v=CqvZ3vGoGs0

print("Imported my_module...")

test = "Test String"


def find_index(to_search, target):
	"""Find the index of a value in a sequence"""
	for i, value in enumerate(to_search):
		if value == target:
			return i

	"""And if it doesn't find the value, then it returns negative 1"""
	return -1
