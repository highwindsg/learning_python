#!/usr/bin/env python3

def func():
    x = "local"
    print(x)

x = "global"
func()      # This function call will print out the word 'local' because the var 'x' is declared inside
            # of the 'func()' function.
print(x)    # This print func will just print out the value of var 'x' that is outside of the 'func()' function.

