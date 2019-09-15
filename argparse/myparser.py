#!/usr/bin/env python3

"""
How to parse command line arguments into Python scripts.
"""

# Using the 'argparse' module to parse the param from the command line to the script.
import argparse

if __name__ == "__main__":
    # Initialise the parser.
    parser = argparse.ArgumentParser()      # Use the '.ArgumentParser()' method with optional param and assign
                                            # to var 'parser'.

    # Parse the arguments
    args = parser.parse_args()
