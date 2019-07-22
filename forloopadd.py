#!/usr/bin/env python3

new_num = 0

print("Before", new_num)

for next_num in [9, 41, 12, 3, 74, 15]:
    new_num = new_num + next_num
    print(new_num, next_num)

print("After", new_num)
