#!/usr/bin/env python3

""" To count how many letter 't' are in the text file 'scarlet.txt'."""

f = open("scarlet.txt", "r")
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 # initialize the accumulator var
for c in txt:   # Iterate through every character in var obj 'txt'.
    if c == "t":    # If that character is the letter 't',
        t_count += 1    # increment the counter by 1.
print("t: " + str(t_count) + " occurences") # Convert 't_count' to a string before print out.
f.close()

print("")

""" To count for many letter 't' and 's' are in the text file 'scarlet.txt'.
Thus accumulating over multiple results. """

f = open("scarlet.txt", "r")
txt = f.read()
t_count = 0 # initialize 't_count' accumulator var.
s_count = 0 # initialize 's_count' accumulator var as well.
for c in txt:   # for every character in 'txt',
    if c == "t":    # if character is 't',
        t_count += 1    # then increase t counter by 1.
    elif c == "s":  # if the character is 's',
        s_count += 1    # then increate s counter by 1.
print("t: " + str(t_count) + " occurences")
print("s: " + str(s_count) + " occurences")
f.close()

print("")

""" Using a empty dictionary to do the above. """

f = open("scarlet.txt")
txt = f.read()
x = {}
x["t"] = 0
x["s"] = 0
for c in txt:
#    if c == "t":
#        x[c] += 1   # 'x[c]' because 'c' is 't'.
#    elif c == "s":
#        x[c] += 1   # 'x[c]' becuase 'c' is 's'.
    if c not in x:
        # Important below.
        # So as long as a character has not been counted before, then initialize it with a new counter.
        x[c] = 0
    x[c] += 1

print("t: " + str(x["t"]) + " occurences")
print("s: " + str(x["s"]) + " occurences")
print("a: " + str(x["a"]) + " occurences")
print("b: " + str(x["b"]) + " occurences")
f.close()
print(x)    # therefore dict 's' will show how many occurrences for every character.

print("")

