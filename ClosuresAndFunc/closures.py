#!/usr/bin/env python3

# Using nested funcs and closures in Python.

# Defining a func in a func.
# Therefore the outerFunction() is an enclosing function.
def outerFunction(text):    # The 'outerFunction()' takes 'text' as an argument param.
    def innerFunction():    # Another local func of the 'outerFunction()' that prints the text param.
        print(text)
    innerFunction()

outerFunction("Hello")
print("")
""" Therefore if you define a function inside another function, it is called the nesting of function. """

def pop(list):      # Define outer function or an enclosing function.
    def get_last_item(my_list):     # Define a local function or inner function.
        return my_list[len(list) - 1]   # Find out the last item on the list 'my_list' and return to the
                                        # answer to get_last_item() inner function.

    list.remove(get_last_item(list))    # From list, use the '.remove' method and pass in the last item
                                        # from the inner function. This will remove the last item from the list.
    return list     # And then return the remaining items from the list to the 'pop(list)' func.


a = [1, 2, 3, 4, 6]     # Create a list with numbers and assign to var 'a'.
print(pop(a))       # Client call the pop() outer function with list 'a' as param.
print(pop(a))
print(pop(a))
