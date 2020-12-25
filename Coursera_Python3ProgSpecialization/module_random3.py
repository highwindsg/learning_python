#!/usr/bin/env python3

import random


def get_random_color():
    colors = ["green", "blue", "red", "yellow"]
    random_color = random.choice(colors)
    return random_color


my_color = get_random_color()
print(my_color)
