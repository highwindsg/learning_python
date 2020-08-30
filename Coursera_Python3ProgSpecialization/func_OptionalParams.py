#!/usr/bin/env python3

# Func f with default param of 'a' and optional param of L=[].
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(f(4, ["Hello"]))
print(f(5, ["Greetings"]))
print("")



"""
Func f2 with one default param 'x' and two optional params of
'y = 3' and 'z = initial' with their own values. 
If you want to provide a non-default value for the third param 'z',
you also need to provide a value for the second param 'y'.

However to specify a value for 'z' without specifying a value for
'y', is called keyword paramaters, will be covered in next chapter.
"""

initial = 7

def f2(x, y = 3, z = initial):
    print("x, y, z are: " + str(x) + ", " + str(y) + ", " + str(z))

f2(2)
f2(2, 5)
f2(2, 5, 8)
print("")


"""
There are two tricky things that can confuse you with default
values. Firstly: ***The default value is determined at the time
that the function is defined, not at the time it is called or
invoked***.
"""

initial = 7

def f3(x, y = 3, z = initial):
    print("x, y, z are: " + str(x) + ", " + str(y) + ", " + str(z))

initial = 10

f3(2)
print("")


"""
Secondly: ***If the default value is set to a mutable object, such
as a list or a dictionary, that object will be shared in all
invocations of the function***.
This can get very confusing, so I suggest that you never set a
default value that is a mutable object.
"""

def f4(a, L=[]):
    L.append(a)
    return L

print(f4(1))
print(f4(2))
print(f4(3))
print(f4(4, ["Hello"]))
print(f4(5, ["Greetings"]))
print("")


"""
What will the following code print?
"""

def f5(x = 0, y = 1):
    return x * y

print(f5())
print("Since no parameters are specified, x is 0 and y is 1, so 0 is returned.")
print("")


"""
What will the following code print?
"""

def f6(x = 0, y = 1):
    return x * y

print(f6(1))
print("Since one parameter value is specified, it is bound to x; y gets the default value of 1.")
print("")


"""
Write a function called str_mult that takes in a required string
parameter and an optional integer parameter. The default value for
the integer parameter should be 3. The function should return the
string multiplied by the integer parameter.
"""

def str_mult(str, int = 3):
    return str * int

print(str_mult("Hello "))
print("")


"""
Define a function called multiply. It should have one required
parameter, a string. It should also have one optional parameter,
an integer, named mult_int, with a default value of 10.
The function should return the string multiplied by the integer.
(i.e.: Given inputs “Hello”, mult_int=3, the function should
return “HelloHelloHello”)
"""

def multiply(str, mult_int = 10):
    return str * mult_int

print(multiply("Hello", mult_int = 3))
print("")
