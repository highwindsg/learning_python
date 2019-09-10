#!/usr/bin/env python3

# Situation when we can use the special Python 'if' statement and keywords of '__name__' and '__main__'.
# eg. if __name__ == "__main__":

def add(a, b):
    return a + b

print(__name__)
if __name__ == "__main__":
    print(add(10, 16))
