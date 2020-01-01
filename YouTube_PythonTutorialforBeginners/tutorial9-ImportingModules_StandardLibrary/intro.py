#!/usr/bin/env python3

# https://www.youtube.com/watch?v=CqvZ3vGoGs0

import my_module as mm
# Or
from my_module import find_index, test

courses = ["History", "Math", "Physics", "CompSci"]

index = find_index(courses, "Math")
print(index)
print(test)
