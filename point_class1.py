class Point:            # Make a class named Point.
    def reset(self):    # Define a function named reset with params self.
        self.x = 0      # From self, get the x attribute and set it to 0.
        self.y = 0      # From self, get the y attribute and set it to 0

p = Point()             # Set p to an instance of class Point.
p.reset()               # From p, get the reset function,
print(p.x, p.y)         # and print the output of p 'which refers to the
                        # class Point', and get the attribute of x and y
                        # which is 0.
