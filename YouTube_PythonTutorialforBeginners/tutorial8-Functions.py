#!/usr/bin/env python3

# https://www.youtube.com/watch?v=9Os0o3wzS_I


def hello_func():
	return "Hello Function!"


print(hello_func())
print(hello_func().upper())     # Using the .upper() method on the return value of hello_func().
print("")


# Define a func named hello2_func() with the required positional arg param first, and then the keyword arg param.
def hello2_func(greeting, name="You"):
	return "{}, {}.".format(greeting, name)     # Return the params of greeting and name into the str format.


print(hello2_func("Hi", name="Caven"))      # Pass in the params values of Hi and name=Caven into the func.
print("")


# Define a func named student_info() with first param of positional arbitrary num of arguments, and then the param of
# arbitrary num of keyword arg.
def student_info(*args, **kwargs):
	print(args)
	print(kwargs)


courses = ["Math", "Art"]
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)  # Func call student_info() with param of arbitrary courses, and then param of
# arbitrary keyword of info. This way, the asterisk will unpack the list and dict items, and return them to the func.
