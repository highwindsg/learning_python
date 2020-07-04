#!/usr/bin/env python3

# https://www.futurelearn.com/courses/programming-for-everybody-python/3/steps/723013

num = 0
tot = 0.0   # total
while True:
    sval = input("Enter a number: ")    # string value
    if sval == "done":
        break
    try:
        fval = float(sval)  # convert str to float
    except:
        print("Invalid input")
        continue    # continue means to go back to the start of this loop.
    print(fval)
    num = num + 1   # num is the counter
    tot = tot + fval    # tot or total is the accumulator

print("ALL DONE")
print(tot, num, tot / num)  # print out the total sum, counter and average

