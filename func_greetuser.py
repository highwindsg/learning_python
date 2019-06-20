#!/usr/bin/env pythom3

def greet_user(name):   # Create a function named greet_user with param var name.
    print(f"Hi {name}!")    # Print out the var name in formatted string.
    print("Welcome aboard")


print("Start")
greet_user("John")  # Function call greet_user and pass in name as string.
greet_user("Mary")  # Function call greet_user and pass in another name as string.
print("Finish")

