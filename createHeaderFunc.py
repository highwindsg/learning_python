#!/usr/bin/env python3

def createHeader(fullName, gender):
    if gender == "m":
        title = "Mr."
    else:
        title = "Ms."
    header = "Dear " + title + " " + fullName + ","     # use of concatenation
    return header

# A few test calls to the function.
print(createHeader("Joe Smith", "m"))
print(createHeader("Susan Jones", "f"))
print(createHeader("Henry Jones", "m"))

