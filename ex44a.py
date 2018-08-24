class Parent(object):   # Make a class named Parent that has its own object params.

    def implicit(self):     # Define a implicit function with its own self params.
        print("PARENT implicit()")

class Child(Parent):    # Make a class named Child that inherits from Parent.
    pass

dad = Parent()  # Set the dad variable to an instance of class Parent.
son = Child()   # Set the son variable to an instance of class Child.

dad.implicit()
son.implicit()

# Run this code and see that both lines 12 and 13 returns the same output which is 'PARENT implicit()'.
# Notice how even though I'm calling son.implicit() on line 13 and even though Child does not have
# an implicit function defined, it still works, and it calls the one defined in Parent. This shows you that
# if you put functions in a base class (i.e., Parent), then all subclasses (i.e., Child) will automatically get
# those features. Very handy for repetitive code you need in many classes.
# This is known as implicit inheritance.
