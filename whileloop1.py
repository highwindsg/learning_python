#!/usr/bin/env python3

num = 1
sum = 0
print("Enter a number. Please enter 0 to exit.")

while num != 0:
    num = float(input("Number ? "))
    sum = sum + num
    print("Sum is: ", sum)
else:
    print("Finished sum.")
print("")


i = 0

while i < 5:
    print("The value of i is: ", i)
    i += 1
else:
    print("Finished while loop.")
