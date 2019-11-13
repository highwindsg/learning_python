#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=K5F-aGDIYaM&list=PLOgeKhf41meTmtKSF8IKOzFcfh28Ks7Cx&index=160&t=0s
To read more on pygame events, go to http://www.pygame.org/docs/ref/event.html
"""

import pygame

pygame.init()  # To initialize the pygame module

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the game surface display with a param of 800 pixels by 600 pixels in a tuple, and assign the surface to var
# 'gameDisplay'.
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Slither")

pygame.display.update()  # After changes has been set for a display, do a update.

gameExit = False

# The start location for the head of the snake.
lead_x = 300
lead_y = 300

while not gameExit:  # This means the gameExit value is still set at False.
    for event in pygame.event.get():  # Use the pygame's .event.get() method to get ALL events in the game window.
        if event.type == pygame.QUIT:  # If user clicks on close window button, then quit game and close the window.
            gameExit = True  # Then set the gameExit var value to True.
        if event.type == pygame.KEYDOWN:    # When detected any cursor key is pressed down,
            if event.key == pygame.K_LEFT:  # and left cursor key is pressed,
                lead_x -= 10  # move to the left by 10 pixels,
            if event.key == pygame.K_RIGHT:     # or when right cursor key is pressed,
                lead_x += 10  # move to the right by 10 pixels.

        # print(event)    # Print out ALL the keyboard and mouse happening in the game window onto the terminal console.

    gameDisplay.fill(white)  # Fill the background of the game window with white color.
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])  # Draw a black rectangle with [x-axis, y-axis,
    # width, height].
    pygame.display.update()

pygame.quit()  # This is to stop the initializing of the pygame.
quit()
