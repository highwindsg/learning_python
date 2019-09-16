#!/usr/bin/env python3

"""
How to parse command line arguments into Python scripts.
"""

# Using the 'argparse' module to parse the param from the command line to the script.
import argparse

if __name__ == "__main__":
    # Initialise the parser.
    # Use the '.ArgumentParser()' method with optional param and assign to var 'parser'.
    parser = argparse.ArgumentParser(
        description="my math script"
    )

    # Add the params positional/optional arguments.
    parser.add_argument("num1", help="Number 1", type=float)
    parser.add_argument("num2", help="Number 2", type=float)
    parser.add_argument("operation", help="provide operator")

    # Parse the arguments
    args = parser.parse_args()
    print(args)

    # Calculate the sum of two numbers.
    result = None   # Create a new var 'result' and set it to None first.
    if args.operation == "+":
        result = args.num1 + args.num2
    if args.operation == "-":
        result = args.num1 - args.num2
    if args.operation == "*":
        result = args.num1 * args.num2
    if args.operation == "/":
        result = args.num1 / args.num2
    if args.operation == "pow":
        result = pow(args.num1, args.num2)

    print("Result: ", result)
    """ Therefore in terminal mode, change dir to /Users/cay1sgp/Documents/GitHub/learning_python/argparse/
    and run the file. (eg. $ python3 myparser.py 84 41 +) and this will give you the sum of the two numbers."""
