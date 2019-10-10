#!/usr/bin/env python3

"""What is the longest random walk you can take so that on average you will end up 4 blocks or fewer from home?
The plan will be to write a random walk function, simple and then short."""

import random


def random_walk(n):  # Create a func named 'random_walk' with param 'n' which is the number of blocks to walk.
    """Return coordinates after 'n' block random walk."""
    x = 0  # Assign starting x and y coordinates at value 0.
    y = 0

    for i in range(n):
        step = random.choice(["N", "S", "E", "W"])
        if step == "N":
            y = y + 1
        elif step == "S":
            y = y - 1
        elif step == "E":
            x = x + 1
        else:
            x = x - 1
    return (x, y)  # Return the coordinates as a tuple.


for i in range(25):  # Let's say we take 25 random walks.
    walk = random_walk(10)  # Each is 10 blocks long.
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))
    """For each walk we will display the coordinates and the distance from home.
    And the distance from home is the sum of the absolute values of x and y coordinates."""
