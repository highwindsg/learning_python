#!/usr/bin/env python3

x = 0
while x < 10:
    print("We are incrementing x.")
    if x % 2 == 0:  # If value of x is an even number,
        x += 3  # then we add 3 to the value of x.
        print(x)
        continue    # Continue will take the sequence back to the
                    # top of the while loop.
    if x % 3 == 0:  # If x is divisible by 3,
        x += 5  # then we add 5 to the value of x.
        print(x)
    x += 1  # Then regardlessly must add 1 to x for the next count.
print("Done with our loop! X has the value: " + str(x))

""" So the 'continue' statement in line 8 ensures that the sequence
will go back up to the top of the while loop to check if x is divisble
by 2 or an even number. """
