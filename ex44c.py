class Parent(object):   # Make a class named Parent with its own object params.

    def altered(self):  # define a function named altered with its own self params.
        print("PARENT altered()")

class Child(Parent):    # Make a class named Child with its own Parent params.

    def altered(self):  # define a function named altered with its own self params.
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()    # Use a Python built-in function named super that calls for the
                                        # Child and self params, whereby the class Child (line 6)
                                        # has the Parent params, which then refers to the class Parent (line 1)
                                        # and then get the attribute of that altered function (line 3).
                                        # Or can read as "call super with arguments Child and self,
                                        # then call the altered function on whatever it returns.
        print("CHILD, AFTER PARENT altered()")

dad = Parent()  # Set the variable dad to an instance of class Parent.
son = Child()   # Set the variable son to an instance of class Child.

dad.altered()   # From dad, get the altered function.
print("")
son.altered()   # From son, get the altered function.

# The third way to use inheritance is a special case of overriding where you want to alter the behavior before
# or after the Parent class's version runs. You first override the function just like in the last example, but
# then you use a Python built-in function named super to get the Parent version to call.
