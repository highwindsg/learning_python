#!/usr/bin/env python3

import random

for i in range(3):
    print(random.random())  # This line will produce 3 random values.
    print("")

    print(random.randint(10, 20))   # This line will produce 3 random values
    print("")                       # between 10 and 20.


members = ["John", "Mary", "Bob", "Mosh"]   # Create a list with names and assign
                                            # to var members.
leaders = random.choice(members)    # Use the choice() method from the random
                                    # module pass in the members list, and assign
                                    # it to var leaders.
print(leaders)  # Print out the name which is chosen from the var leaders.

