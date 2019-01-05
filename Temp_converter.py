#!/usr/bin/env python3

# Code to ask the user to input values for conversion
# Fahrenheit to Centigrade formula:
#   C = (F - 32) * 0.5556   # 0.5556 is the decimal equivalent of 5 divide by 9
# Centigrade to Fahrenheit formula:
#   F = (1.8 * C) + 32

def F2C(nDegreesF):
    nDegreesF = (nDegreesF - 32) * 0.5556
    return nDegreesF

def C2F(nDegreesC):
    nDegreesF = (1.8 * nDegreesC) + 32
    return nDegreesF

usersTempF = input("Enter a value of degrees Fahrenheit: ")
usersTempF = float(usersTempF)
convertedTempC = F2C(usersTempF)
print(usersTempF, "degrees Fahrenheit is:", convertedTempC, "degrees Centigrade.")

usersTempC = input("Enter a value of degrees Celsius: ")
usersTempC = float(usersTempC)
convertedTempF = C2F(usersTempC)
print(usersTempC, "degrees Centigrade is:", convertedTempF, "degrees Fahrenheit.")

print("")
# Below is just a interesting testing.
# The innermost function call to C2F() runs first,
# and then the value is passed to the outside function of F2C,
# which final results is the number we started with '100'.
print(F2C(C2F(100.00)))
