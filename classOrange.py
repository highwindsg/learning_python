#!/usr/bin/env python3

class Orange:                   # Create a class named 'Orange'.
    # '__init__' is called a 'magic method' that Python uses for special purposes like
    # creating an object.
    def __init__(self, w, c):   # Define a init start function with params self, w and c.
        self.weight = w         # From 'self', get the attribute of weight and assign to w.
        self.color = c          # From 'self', get the attribute of color and assign to c.
        print("Created!")

# After defining the class above, we 'instantiate' the Orange class below with the code
# and print it out.
or1 = Orange(10, "dark orange")
print(or1.color)
print(or1.weight)
print("")
print("Changing the value of the instance variable:")
or1 = Orange(10, "dark orange")
or1.weight = 100
or1.color = "light orange"
print(or1.weight)
print(or1.color)
print(or1)  # Result of this print shows the Orange object at some memory location.
