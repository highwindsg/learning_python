#!/usr/bin/env python3

def greet_user(first_name, last_name):  # Create a function named greet_user
                                        # with two param var name.
    print(f"Hi {first_name} {last_name} !") # Print out the var name in
                                            # formatted string.
    print("Welcome aboard")


print("Start")
# Function call greet_user and pass in keyword arguments of 'last_name' and
# 'first_name'. Therefore there is no need to worry about not being in the
# correct positional argument.
greet_user(last_name = "Smith", first_name = "John")
greet_user("Mary", "Nelson")    # Function call greet_user and pass in the positional
                                # arguments of 'Mary' and 'Nelson'.
print("Finish")

