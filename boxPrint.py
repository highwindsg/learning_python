#!/usr/bin/env python3

"""
Often it is the code that calls the function, not the function itself
that knows how to handle an exception.
So you will commonly see a 'raise' statement inside a function and the
'try' and 'except' statements in the code calling the function.
"""

# Create a func named boxPrint with params symbol, width and height.
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string.")
    if width <= 2:
        raise Exception("Width must be greater than 2.")
    if height <= 2:
        raise Exception("Height must be greater than 2.")
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (" " * (width -2)) + symbol)

    print(symbol * width)

for sym, w, h in (("*", 4, 4), ("O", 20, 5), ("x", 1, 3), ("ZZ", 3, 3)):
    try:    # The 'try' statement calling the boxPrint function.
        boxPrint(sym, w, h)
    except Exception as err:
        print("An exception happened: " + str(err))

