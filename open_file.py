#!/usr/bin/env python3

employee_file = open("employees.txt", "r")  # Open a file with read mode and
                                            # assign it to var 'employee_file'.
print(employee_file.readable()) # This will return a Boolean value to let you
                                # know if the file is readable.
#print(employee_file.read()) # The will read the file and print out the content.

#print(employee_file.readline()) # This will only read and print out the first
                                # line and cursur returns a next empty line.
#print(employee_file.readline()) # This second same line of code will print out
                                # second line from the txt file.
print(employee_file.readlines()[1]) # To read the second line by parsing in the
                                    # index 1 from a list [1].

#for employee in employee_file.readlines():  # This forloop will print out all
#    print(employee)                         # the lines with a empty line in-
                                            # between.

employee_file.close()   # Close the file var.

