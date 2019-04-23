#!/usr/bin/env python3

"""
Write a program that prints the numbers from 1 to 100.
But for multiple of three print "Fizz" instead of the number,
and for the multiple of five print "Buzz" instead of the number.
For multiples of both three and five print "FizzBuzz".

Hint:
eg. If a number is a multiple of three and you divide it by
three, there is no remainder. And the modulo operator (%)
returns the remainder.
"""

def fizz_buzz():
    for num in range(1, 101):
        # So if a number divide by 3 and divide by 5 and
        # the remainder is equal to zero.
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        # Or read as if a number mod 3 and remainder is
        # equal to zero.
        elif num % 3 == 0:
            print("Fizz")
        # If a number mod 5 and remainder is equal to zero.
        elif num % 5 == 0:
            print("Buzz")
        # If none of the other numbers can be divided by
        # 3 or 5, then print out those numbers.
        else:
            print(num)

# Call the fizz_buzz function.
fizz_buzz()
