#!/usr/bin/env python3

from time import time

def timing(func):
    def wrapper_func(*args, **kwargs):
        start = time()
        print(start)
        result = func(*args, **kwargs)
        end = time()
        print(end)
        print("Elapsed time: {}".format(end - start))
        return result

    return wrapper_func

@timing
def my_func(num):
    sum = 0
    for i in range(num + 1):
        sum += 1

    return sum

print(my_func(20000000))
