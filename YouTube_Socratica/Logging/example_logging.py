#!/usr/bin/env python3

"""
Purpose of logging: Record progress and problems.
Levels: Debug, Info, Warning, Error, Critical, etc.
"""

import logging  # import the logging module if you need to use logging.
import math

print(dir(logging))
"""
The items in all caps are constants.
The items with first capitalized char are classes.
The items that starts with a lowercase letter are methods.
"""

# Create and configure logger by using the .basicConfig() method from the logging module.
# Pass in the log file name location and if the file does not exist, it will be created.
# Also have to set the logging level to DEBUG (level 10), else only WARNING (level 30) log messages will be printed.
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/Logging/lumberjack"
                             ".log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode="w")  # Set the filemode to write, if not given, then default is append mode.
logger = logging.getLogger()  # Use the .getLogger() method to create a logger obj. This is a root logger.

# Testing the logger by printing and info message to the file.
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero?")
logger.critical("The entire Internet is down!!")

# To show the logging level.
print("Current logging level is ", logger.level)
print("")


# Create a quadratic formula function.
def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b ** 2 - 4 * a * c

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)

    # Return the root as a tuple.
    logger.debug("# Return the roots")
    return (root1, root2)


roots = quadratic_formula(1, 0, -4)
print(roots)
