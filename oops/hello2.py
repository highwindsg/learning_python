#!/usr/bin/env python3

class Hello:    # Create a class named 'Hello'.
    def __init__(self, name):   # Define a init start func with params 'self' and 'name'.
        self.a = 10             # From self, set the var '.a' to 10.
        self._b = 20            # From self, set the var '._b' to 20.
        self.__c = 30           # From self, set the private var '.__c' to 30.
    def public_method(self):    # Define a public_method func with param self.
        print(self.a)           # From self, get the attrib of 'a'.
        print(self.__c)         # From self, get the private attrib of '.__c'.
        print("public")         # Print the word 'public'.
        self.__private_method()     # So even if a private method is defined later in the next line,
                                    # it can also be used anywhere within the same class,
                                    # but not outside of the class.

    def __private_method(self):     # Define a private method named '__private_method()' with param self.
        print("private")            # Print the word 'private' in this private method.


hello = Hello("name")       # Set var obj hello to the Hello() class with param str 'name'.
print(hello.a)              # Get the value of attrib .a from the hello var obj and print it out.
print("")
print(hello._b)             # Get the value of attrib ._b from the hello var obj and print it out.
print("")
hello.public_method()       # Just print the param of .public_method() func from var obj hello.

"""
Therefore self.__c will not be printed in output as it is a private member var in the class.
"""
