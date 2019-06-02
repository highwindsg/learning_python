#!/usr/bin/env python3

# To protect the program from crashing with error even though a wrong data type
# is entered. Rather, we choose to exit the program properly with an alternate
# message.

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError as err:    # Store the detailed error mnessages of
                                    # 'ZeroDivisionError' into a obj.
    print(err)                      # Then print out the obj which stores the
                                    # actual error messages.

except ValueError:
    print("Invalid input")
