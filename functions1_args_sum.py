#!/usr/bin/env python3

def sum(arg1, arg2):
    if type(arg1) != type(arg2):    # This means eg. str must be str, and int must be int, cannot be different type.
        print("Please give arguments of the same type.")
        return          # Note that if 'return' is called without any syntax,
                        # then whatever after this line will not be executed.
    return (arg1 + arg2)


print(sum(15, 60))     # Client call the func 'sum()' with two numeric params.
print(sum("Hello ", "World"))   # Client call the func 'sum()' with two string params,
                        # making use of the '+' concatenation to join the two words.
print(sum("Hello ", 15))
