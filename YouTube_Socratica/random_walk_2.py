"""What is the longest random walk you can take so that on average you will end up 4 blocks or fewer from home?
The plan will be to write a random walk function, simple and then short.
This is the same program as 'random_walk.py' but more compacted."""

import random

def random_walk_2(n):
    """Return coordinates after 'n' block random walk."""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)


for i in range(25):
    walk = random_walk_2(10)
    print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

print("")

# To answer the above question...
number_of_walks = 10000

for walk_length in range(1, 31):
    no_transport = 0    # Number of walks 4 or fewer blocks from home.
    for i in range(number_of_walks):
        (x, y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length, " / % of no transport = ", 100 * no_transport_percentage)