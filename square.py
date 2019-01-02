#!/usr/bin/env python3

def square(number):
    answer = number * number
    return answer   # returns the answer to the caller of 'square()'

userNumber = input("Enter a number: ")
userNumber = float(userNumber)      # converts to a float
numberSquared = square(userNumber)  # call the function and save the result
print("The square of your number is", numberSquared)
