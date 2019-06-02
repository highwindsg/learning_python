#!/usr/bin/env python3

employee_file = open("employees.txt", "a")  # Open a file with append mode and
                                            # assign it to var 'employee_file'.
employee_file.write("\nJane - Human Resources") # The will write the new line
                                                # on the next line. The '\n' is
                                                # an escape key.
employee_file.close()   # Close the file var.
