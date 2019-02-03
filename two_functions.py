#!/usr/bin/env python3

def divide(num1):
    """
    The line below will calculate the division by 2
    and return the answer back to the divide function.
    """
    return num1 / 2

def multi(num2):
    """
    The line below will calculate the multiplication by 4
    and then return the answer back to the multi function.
    """
    return num2 * 4

number = int(input("Type a number to be divided by 2, then multiplied by 4: "))
divided = divide(number)
multiplied = multi(divided)
final = str(multiplied)
print("The final answer is", final)

