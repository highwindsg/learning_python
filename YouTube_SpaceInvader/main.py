#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=FfWpgLFMI7w&list=PLOgeKhf41meTmtKSF8IKOzFcfh28Ks7Cx&index=155&t=169s
"""

import pygame

# Initialize the pygame
pygame.init()

# Set the game display windows with height of 800 and width of 600 pixels.
screen = pygame.display.set_mode((800, 600))

# Game window title and icon
pygame.display.set_caption("Space Invaders")

# For the window title, load the icon picture and assign to a var named 'icon'
icon = pygame.image.load("ufo.png")
# Use the pygame display .set_icon() method and pass in the icon var that contains the png file.
pygame.display.set_icon(icon)

# Game loop
running = True  # Set the var 'running' to True first so that the window stays open.

"""So if the close window is clicked, then change the value of var 'running' to False and close the game window."""
while running:
    for event in pygame.event.get():    # To get the state of the event in pygame using the .get() method.
        if event.type == pygame.QUIT:
            running = False

    # To set the bg color to black.
    # RGB - Red, Green, Blue and number does from 0 to 255. 0 is black.
    screen.fill((255, 0, 0))
    pygame.display.update()     # Then update the display game window.
