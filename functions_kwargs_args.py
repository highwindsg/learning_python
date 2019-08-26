#!/usr/bin/env python3

# Default arguments *args and **kwargs.
def student(name="Unknown name", age=0, **marks):   # Note that '*marks' is an arbitrary number of arguments.
                                                    # **kwargs means key words and arbitrary number of arguments.
    print("name: ", name)
    print("age", age)
#    print("marks", marks)                  # Instead of printing out in a tuple,
    for key, value in marks.items():        # can also use the 'for loop' to print out in a column.
        print(key, " ", value)


student("Max", 22)  # Since 'Max' and '22' args are given as params in this client call,
print("")           # then the default args which are set in the function will not be used.

student()   # Since no arguments are provided, the default arguments of 'Unknown name' and '0' are used.
print("")

student("tom")  # Since no second args param are given, the default arg of '0' will be used.
print("")

# So we assign key words arguments as subject names to the marks, because we have defined in the
# function in the beginning to use **kwargs - arbitrary multiple number of key word arguments.
student("tom", 22, english=95, math=70, physics=80, biology=50)
print("")
