#!/usr/bin/env python3

# Absolute Value Program
# Function to generate the absolute value of a number.

def absoluteValue(valueIn):
    if valueIn >= 0:
        valueOut = valueIn  # Since valueIn is >= 0, therefore is already a absolute value.
                            # So the absolute value can be passed into the variable valueOut.
    else:   # Must be negative, then multiply by minus one to get a positive absolute value.
        valueOut = -1 * valueIn
    return valueOut

# Test cases

result = absoluteValue(10.5)
print("The absolute value of 10.5 is", result)

result = absoluteValue(-8)
print("The absolute value of -8 is", result)

# Get user input and convert to a floating point number.
userNumber = int(input("Enter a number: "))

# Call the function with the user's number and print the answer.
result = absoluteValue(userNumber)
print("The absolute value of", userNumber, "is", result)
