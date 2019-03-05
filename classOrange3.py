#!/usr/bin/env python3

# Now we give the orange the ability to rot.

class Orange():                 # Create a class named 'Orange()'.
    def __init__(self, w, c):   # Define a init start function with params self, w and c.
        self.weight = w         # From self, get the attribute of weight and assign to w
        self.color = c          # From self, get the attribute of color and assign to c
        self.mold = 0           # From self, get the attribute of mold and assign to 0 even
                                # though the 'mold' param is not set in the init start function.
        print("Created!")

    def rot(self, days, temp):  # Define a function named 'rot' with params self, days and temp.
        self.mold = days * temp # From self, get the mold attribute and assign it with the result
                                # of days * temp.

# Parse in the params of weight and color into the class Orange() and assign to var 'orange'.
orange = Orange(6, "light orange")
print(orange.mold)  # Print out the attribute of mold from var 'orange'.
orange.rot(10, 98)  # Assign params 10 days, 98 temp into the 'rot' function of var 'orange'.
print(orange.mold)  # Now print out again the new attribute of 'mold' from the var 'orange'
                    # after 'rot' function has been assigned the days and temp.

