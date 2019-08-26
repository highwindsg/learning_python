#!/usr/bin/env python3

# Default arguments *args and **kwargs.
def student(name="Unknown name", age=0, *marks):    # Note that '*marks' is an arbitrary number of arguments.
    print("name: ", name)
    print("age", age)
#    print("marks", marks)      # Instead of printing out in a tuple,
    for x in marks:             # can also use the 'for loop' to print out in a column.
        print("marks: ", x)


student("Max", 22)  # Since 'Max' and '22' args are given as params in this client call,
                    # then the default args which are set in the function will not be used.
print("")

student()   # Since no arguments are provided, the default arguments of 'Unknown name' and '0' are used.
print("")

student("tom")  # Since no second args param are given, the default arg of '0' will be used.
print("")

student("tom", 22, 95, 70, 80, 50)  # So 95, 70, 80 and 50 will be displayed as a tuple,
                                    # which is part of the third param of arbitrary number of arguments.
print("")

