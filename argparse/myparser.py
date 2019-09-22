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
        description="my math script"    # The string will show if -h is used in the command line.
    )

    # Add the params positional/optional arguments. This will show if the -h is used in command line.
    parser.add_argument("-n1", "--num1", help="Number 1", type=float)
    parser.add_argument("-n2", "--num2", help="Number 2", type=float)
    parser.add_argument("-op", "--operation", help="provide operator + - * / or power", default="+")

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
    if args.operation == "power":
        result = pow(args.num1, args.num2)

    print("Result: ", result)
    """ Therefore in terminal mode, change dir to /Users/cay1sgp/Documents/GitHub/learning_python/argparse/
    and run the file.
    (eg. $ python3 myparser.py --num1 84 --operation - --num3 41) and this will give you the different of the two numbers.
    But if not --operation option is used, then the default + operation will be used.
    (eg. $ python3 myparser.py --num1 84 --num3 41) will give you the sum of the two numbers.
    Alternatively, can also use the short-hand notation option.
    (eg. $ python3 myparser.py -n1=84 -n2=70 -op=+) Must use '=', cannot use a empty space.
    """
