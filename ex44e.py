class Other(object):    # Make a class named Other with object self.

    def override(self): # Define a function named override with self params.
        print("Other override()")

    def implicit(self): # Define a function named implicit with self params.
        print("Other implicit()")

    def altered(self):  # Define a function named altered with self params.
        print("Other altered()")

class Child(object):    # Make a class named Child with object self.

    def __init__(self): # Define a init with self params.
        self.other = Other()    # From self, assign 'other' to an instance of class 'Other'.

    def implicit(self): # Define a function named implicit with self params.
        self.other.implicit()   # From self, get the other attribute, and then get the implicit function.

    def override(self): # Define a function named override with self params.
        print("CHILD override()")

    def altered(self):  # Define a function named altered with self params.
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()    # From self, get the other attribute, and then get the altered function.
        print("CHILD, AFTER OTHER altered()")

son = Child()   # Set son to an instance of class Child.

son.implicit()  # From son, get the implicit function.
son.override()  # From son, get the override function.
son.altered()   # From son, get the altered function.
