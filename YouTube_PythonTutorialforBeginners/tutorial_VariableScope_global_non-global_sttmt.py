#!/usr/bin/env python3

# https://www.youtube.com/watch?v=QVdf0LgmICw

"""
LEGB
Local, Enclosing, Global, Built-in
"""

x = "global x"  # Set var x with some value. This is a global scope var.


# Create a func named test().
def test():
	y = "local y"  # Set a local scope var y with some value in this func.
	x = "local x"  # Set a local scope var x with some value in this func.
	# print(y)   # Print out the value of var y.
	print(x)  # If there is no x var in the local scope, then will print out the x var the from global scope.


test()
# print(y)    # This line output will fail as var y is not a global scope var.
print(x)
print("")


# Create a func named test2() with param of z.
def test2(z):
	x = "local x"
	print(z)  # Print out the param of z.


test2('local z')  # Func call test2() with param of 'local z'. This will print out the value 'local z' as it is passed
# into the function's param z.
print("")

m = min([5, 1, 4, 2, 3])  # min() is a builtin func in python.
print(m)
print("")


# Create a outer() func with its own var x and value.
def outer():
	x = "outer x"

	# Create a inner() inner func with its own local var x and value.
	def inner():
		x = "inner x"
		print(x)    # Then print out the value of x.

	inner()     # Func call inner() within the outer() func.
	print(x)    # Print out the value of x within the outer() func.


outer()     # Func call the outer() func.
print(x)

