#!/usr/bin/env python3

"""
super() class function.
Can use the super() func in a subclass to call the init start func of the parent class.
"""

class Parent:       # Create a class named Parent.
    def __init__(self, name):       # Define a init start func with param 'self' and 'name'.
        print("Parent __init__", name)  # Print a str with param 'name'.

class Parent2:       # Create a class named Parent.
    def __init__(self, name):       # Define a init start func with param 'self' and 'name'.
        print("Parent2 __init__", name)  # Print a str with param 'name'.

class Child(Parent2, Parent):        # Create a class named Child that inherits from the Parent class.
    def __init__(self):     # Define a init start func with param 'self'.
        print("Child __init__")
        super().__init__("Max1")    # Using the 'super() func, it allows a subclass to use the
                                    # attrib of the Parent class and set the param 'name' with
                                    # a str name.
        Parent2.__init__(self, "Max2")  # From Parent2 class, get the init start attrib and print
                                        # out the param 'name' as Max2.
        Parent.__init__(self, "Tom")    # From Parent class, get the init start attrib and print
                                        # out the param 'name' as Tom.


child = Child()     # Client call, set var child is-a Child() class.
print(Child.__mro__)    # This line will print out the 'method resolution order' in memory of
                        # how the order of classes are executed.

"""
What is an __init__() function?
An __init__() function is the first function that is called when a class is created.
"""
