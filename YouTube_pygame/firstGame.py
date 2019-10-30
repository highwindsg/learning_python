#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=i6xMBig-pP4
"""

import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))   # The width and height of the window.

pygame.display.set_caption("First Game")    # Title of the window.

# Position of the game character and how fast it can move.
x = 50
y = 50
width = 40
height = 60
vel = 5     # Velocity speed.

run = True
while run:
    pygame.time.delay(100)  # A clock time delay of 100 milli-secs.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel    # minus 1 on x coordinate to move left.
    if keys[pygame.K_RIGHT]:
        x += vel    # add 1 on x coordinate to move right.
    if keys[pygame.K_UP]:
        y -= vel    # minus 1 from y coordinate to move up.
    if keys[pygame.K_DOWN]:
        y += vel    # add 1 to y coordinate to move down.

    win.fill((0,0,0))   # To set background color to black.
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))   # windows is red color param, and rectangle param.
    pygame.display.update()

pygame.quit()
