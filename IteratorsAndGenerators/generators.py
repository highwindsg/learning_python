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
print(next(x))      # Likewise, the third client call of the 'next()' func will cause the generator to remember
                    # that you had already called the second 'yield' iterator before, and so will print
                    # you the next 'yield' value.
#print(next(x))     # This client call will raise the StopIteration error as there are no more yield.

"""
Role of the 'yield' keyword:
So whatever value you write after the 'yield' keyword (line 10), it is going to return that value, and immediately
after that it is going to save the status of your function.
So whenever you call the 'next()' function for the first time (line 16) with the 'x' var obj, it is going to return
the first value 'a' which you used with the 'yield' keyword and immediately save the status of the iterator at 'a'.
And then when you call the 'next()' function once again (line 17), the generator will remember that last time it has
returned the first 'a' value, and now is the time to return the next 'b' value.
"""
print("")

# Alternatively you can use 'for loop' to print out the 'yield' value.
def my_func2():
    for i in range(5):
        print("-------------------", i)
        yield i

y = my_func2()

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
#print(next(y))     # This client call will raise the StopIteration error as there are no more yield.
