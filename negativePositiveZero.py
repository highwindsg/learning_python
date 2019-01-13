#!/usr/bin/env python3

# Create a program that contains a function called negativePositiveZero.
# It is passed one numeric(integer or float) parameter, and should only
# return 'negative', 'positive' or 'zero' depending on the numeric entered.

def negativePositiveZero(numericIn):
    if numericIn < 0.0:
        answer = "Negative"
    elif numericIn > 0.0:
        answer = "Positive"
    else:
        answer = "Zero"
    return answer

# Test cases

EnterNum = int(input("Enter a integer numeric: "))
FinalAns = negativePositiveZero(EnterNum)
print(EnterNum, "is", FinalAns)
