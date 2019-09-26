#!/usr/bin/env python3

""" decorators wrap a function and modify its behaviour in one way or the another without having to
directly change the source code of the function being decorated. """

def decorator_X(func):
    def wrapper_func():
        print("X" * 20)
        func()
        print("X" * 20)

    return wrapper_func

def decorator_Y(func):
    def wrapper_func():
        print("Y" * 20)
        func()
        print("Y" * 20)

    return wrapper_func

# @decorator_Y
# @decorator_X

def say_hello():
    print("Hello World")

hello = decorator_X(decorator_Y(say_hello))
hello()
#say_hello()
