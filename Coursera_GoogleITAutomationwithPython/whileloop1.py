#!/usr/bin/env python3

x = 0
while x < 5:
    print("Not there yet, x = " + str(x))
    x += 1
    
#print(x)
print("x = " + str(x) + ", so we stop here.")
print("")


def attempts(n):
    x = 1
    while x <= n:
        print("Attempts " + str(x))
        x += 1
    
    print("Done")
    
    
attempts(5)
print("")



"""
In this code, there's an initialization problem that's causing our function to behave 
incorrectly. Can you find the problem and fix it?
"""

def count_down(start_number):
    current = start_number  # Therefore answer is 'current = start_number'.
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")


count_down(4)
print("")
"""
Note: Therefore whenever you're writing a loop, check that you're initializing all the
variables you want to use before you use them.
"""



"""
The following code causes an infinite loop.
Can you figure out what’s missing and how to fix it?

def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)
        
print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)
"""

def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)
        n += 1  # Therefore the answer is to include this line to increase the accumulator
        # until 'n' reaches lesser or equal to the value of the second param (end).


print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
print("")



"""
Note: A while loop is great for performing an action over and over until a condition has changed.
"""
