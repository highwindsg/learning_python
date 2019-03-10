#!/usr/bin/env python3

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # clients can use this
        pass

    def _unsafe_method(self):
        # clients shouldn't use this
        pass
"""
Private variables and methods are useful when you have a method or variable
that your class uses internally, but you plan to change the implementation
of your code later (or you want to preserve the flexibility of that option),
and thus don't want whoever is using the class to rely on them, because
they might change (and would then break the client's code).
Private variables are an example of the second concept encapsulation refers
to; private variables hide a class's internal data to prevent the client from
directly accessing it.
Public variables, on the other hand, are variables a client can access.
Python however does not have private variables. All of Python's variables
are public. Python solves the problem private variables address another way,
-- by using naming conventions.
In Python, if you have a variable or method the caller should not access,
you precede its name with an underscore, they shouldn't use (although they
are still able to at their own risk).
CLient programmers reading this code know the variable 'self.public' is safe
to use, but they shouldn't use the variable 'self._unsafe' because it starts
with an underscore, and if they do, they do so at their own risk.
The person maintaining this code has no obligation to keep the variable
'self._unsafe' around, because callers are not supposed to be accessing it.
Client programmers know the method 'public_method' is safe to use, whereas
the method '_unsafe_method' is not, because its name starts with an
underscore.
"""
