#!/usr/bin/env python3

def decorator_divide(func):
    def wrapper_func(a, b):
        print("divide ", a, ' and ', b)
        if b == 0:
            print("division with zero is not allowed")
            return 0
        return a / b

    return wrapper_func

@decorator_divide
def divide(x, y):
    return x / y

print(divide(15, 0))
