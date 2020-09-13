#!/usr/bin/env python3

# Define a func named 'hello3' with params 's' and 'n'.
def hello3(s, n):
    # Create the str in .format and pass in param 's'.
    greeting = "Hello {} ".format(s)
    # Print the 'greeting' var multiply by number of times
    # specified by param 'n'.
    print(greeting*n)


hello3("Bob", 4)
hello3("", 1)
hello3("Kitty", 11)

print("")

def hello4(s):
    print("Hello " + s)
    print("Glad to meet you")


hello4("Iman" + " and Jackie")
hello4("Class " * 3)

print("")



"""
What output will the following code produce?
"""

def cyu(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    else:
        print(s2)

print(cyu("Hello", "Goodbye"))



"""
Define a function called information that takes as input, the 
variables name, birth_year, fav_color, and hometown. It should return 
a tuple of these variables in this order.
"""

def information(name, birth_year, fav_color, hometown):
    return name, birth_year, fav_color, hometown

print(information("John", 1975, "Blue", "Georgetwon"))
print("")
