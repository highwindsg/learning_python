#!/usr/bin/env python3

def func():
    print(x)

x = "global"
func()      # This function call will print out the word 'global' which is a global var because it is set
            # outside of the 'func()' function. Therefore var 'x' is a global scope var.


