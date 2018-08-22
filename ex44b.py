class Parent(object):   # Make a class named Parent that has its own object params.

    def override(self):     # define a override function with its own self params.
        print("PARENT override()")

class Child(Parent):    # Make a class named Child that has the Parent params.

    def override(self):     # define a override function with its self params.
        print("CHILD override()")

dad = Parent()  # Set dad to an instance of class Parent.
son = Child()   # Set son to an instance of class Child.

dad.override()
son.override()

# The problem with having functions called implicitly is sometimes you want the child to behave differently.
# In this case you want to override the function in the child, effectively replacing the implicit functionality.
# To do this just define a function with the same name in Child.
# As you run the program, line 14 runs the Parent.override function because that variable (dad) is a Parent.
# But when line 15 runs, it shows the Child.override output because son is an instance of Child,
# and Child overrides that function by defining its own string output.
