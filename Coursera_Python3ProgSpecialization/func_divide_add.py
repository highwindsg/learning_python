#!/usr/bin/env python3

"""
You will need to write two functions for this problem. The first
function, divide that takes in any number and returns that same
number divided by 2. The second function called sum should take
any number, divide it by 2, and add 6. It should return this new
number. You should call the divide function within the sum function.
Do not worry about decimals.
"""

def divide(num):
    div_ans = num / 2
    return int(div_ans)


def sum(num):
    div_add_ans = divide(num) + 6
    return int(div_add_ans)


number = 10
print(divide(number))
print(sum(number))
