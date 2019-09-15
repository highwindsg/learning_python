#!/usr/bin/env python3

""" generator is a simpler way of creating an iterator.
generator is a function that returns the iterator object on which we can iterate upon.
"""

# The role of the 'yield' keyword is to save whatever value you enter after the 'yield' keyword and
# save it to the function.
def my_func():
    yield "a"   # When you use a 'yield' keyword in a function, it becomes a generator,
    yield "b"   # and when you use the generator, it returns the iterator obj.
    yield "c"

x = my_func()

print(next(x))      # The first client call of the 'next()' func with param of var obj 'x'.
print(next(x))      # The second client call of the 'next()' func will cause the generator to remember
                    # that you had already called the first 'yield' iterator before, and so will print
                    # you the next 'yield' value.
print(next(x))
print(next(x))
