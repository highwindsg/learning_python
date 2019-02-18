#!/usr/bin/env python3

for i in range(1, 6):
    if i == 3:      # When 'i' equals 3, your continue-statement executes.
        continue    # Instead of causing your loop to exit, like the 'break'
                    # keyword would, the loop persists and moves on to the
                    # next iteration.
    print(i, "for loop continue statement")

# You can achieve the same result using a 'while-loop' and a 'continue-statement'.

i = 1
while i <= 5:
    if i == 3:      # So when 'i' equals 3,
        i += 1      # increment 'i' counter to the next loop,
        continue    # and continue by skipping this 'if' loop.
    print(i, "while loop continue statement")
    i += 1
