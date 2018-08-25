class Parent(object):   # Make a class Parent with its own object.

    def override(self): # Define a override function with its own self params.
        print("PARENT override()")

    def implicit(self): # Define a implicit function with its own self params.
        print("PARENT implicit()")

    def altered(self):  # Define a altered function with its own self params.
        print("PARENT altered()")

class Child(Parent):    # Make a class named Child that takes the Parent params.

    def override(self): # Define a override function with its own self params.
        print("CHILD override()")

    def altered(self):  # Define a altered function with its own self params.
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()    # Use a Python build-in function named super
                                        # that calls for the Child and self params,
                                        # whereby the class Child has the Parent params,
                                        # which then refers to the class Parent and then
                                        # get the attribute of that altered function.
                                        # Or can read as "call super with arguments Child
                                        # and self, then call the altered function on
                                        # whatever it returns.
        print("CHILD, AFTER PARENT altered()")

dad = Parent()  # Assign the variable dad to class Parent.
son = Child()   # Assign the variable son to class Child.

dad.implicit()  # From dad, get the attribute of the implicit function.
son.implicit()  # From son, get the attribute of the implicit function.

dad.override()  # From dad, get the attribute of the override function.
son.override()  # From son, get the attribute of the override function.

dad.altered()   # From dad, get the attribute of the altered function.
son.altered()   # From son. get the attribute of the altered function.
