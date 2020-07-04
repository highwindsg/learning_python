#!/usr/bin/env python3

# https://www.futurelearn.com/courses/programming-for-everybody-python/3/steps/723011

count = 0
sum = 0
print("Before", count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum / count)

