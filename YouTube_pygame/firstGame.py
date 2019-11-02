#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=i6xMBig-pP4
"""

import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))  # The width and height of the window.

pygame.display.set_caption("First Game")  # Title of the window.

# Position of the game character and how fast it can move.
x = 50
y = 450
width = 40
height = 60
vel = 5  # Velocity speed.

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(100)  # A clock time delay of 100 milli-secs.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    """Below 'if' statement are for cursor keys movements as well as limiting the border
    of not allowing the game character to move out of the box."""
    if keys[pygame.K_LEFT] and x > vel:  # To limit the left/right movement within the box.
        x -= vel  # minus 1 on x coordinate to move left.
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:  # To limit the left/right movement within the box.
        x += vel  # add 1 on x coordinate to move right.
    if not isJump:
        if keys[pygame.K_UP] and y > vel:  # To limit the top/down movement within the box.
            y -= vel  # minus 1 from y coordinate to move up.
        if keys[pygame.K_DOWN] and y < 500 - height - vel:  # To limit the top/down movement within the box.
            y += vel  # add 1 to y coordinate to move down.
        # Triggering a jump action for the game character.
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))  # To set background color to black.
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))  # windows is red color param, and rectangle param.
    pygame.display.update()

pygame.quit()
