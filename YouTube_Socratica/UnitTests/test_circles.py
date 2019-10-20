#!/usr/bin/env python3

# Import the 'unittest' module to perform unit testing python program.
import unittest

# The 'circles.py' file and its func 'circle_area()' must be in the same folder.
# Then import the 'circle_area()' function from the 'circles.py' file.
from circles import circle_area
from math import pi

"""Then create a class that is a subclass of the test case class in the unit test module.
We will call our class the 'TestCircleArea'."""


class TestCircleArea(unittest.TesttCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)

    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)


"""
In order to test the program, must run from the command line with directory where the same files are stored.
The -m option instructs Python to run the unittest module as a script.
eg. $> python -m unittest test_circles
    or 
    $> python -m unittest
"""
