#!/usr/bin/env python3

fh = open("demo.txt", "r")  # Open the new file 'demo.txt' in readonly mode.
                            # If no mode is indicated, then the default readonly mode will be use.

try:
    for line in fh:
        print(len(line.split(" ")))     # First 'split' each and every word on every line with a space,
                                        # then count how many words in each line with 'len'.

finally:    # The 'finally' suit will execute it's body even if the 'try' suit above made a error.
    fh.close()

print("")

# Alternatively, can run the script as below, which is the same as line 3-10.
with open("demo.txt", "r") as fh:
    for line in fh:
        print(len(line.split(" ")))
