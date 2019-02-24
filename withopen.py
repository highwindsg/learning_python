#!/usr/bin/env python3

# As long as Python finishes running the code in the
# 'with-statement', Python closes the file automatically.
with open("st1.txt", "w") as f:
    f.write("Hi from Python again!\n")
