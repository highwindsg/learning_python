#!/usr/bin/env python3

def func():
    x = 50      # Assign var 'x' with a value of 50, as a local var to the 'func()' function.
    def inner():
        nonlocal x      # Assigning 'x' as a nonlocal var.
        x = 100
    print("1-------", x)    # This will print out 50 from line 4 as it is still a local var.
    inner()                 # Calling the 'inner()' function.
    print("2-------", x)    # This will print out 100 from line 7 as the 'inner()' function has been
                            # called before this line.

x = 20      # Assign var 'x' with a value of 20, as a global var.
func()      # Calling the 'func()' function.
print("3-------", x)        # This will line print out 20 from line 13 where 'x' is the global function.
"""
Although there is a function call of 'func()' in line 14, those var 'x' are
inside the 'func()' function only. And so the 'print()' function in line 15 will
print out the 'x' value 20 from the global var.
"""
