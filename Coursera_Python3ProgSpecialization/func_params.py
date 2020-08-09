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
