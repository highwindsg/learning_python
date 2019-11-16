#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=K5F-aGDIYaM&list=PLOgeKhf41meTmtKSF8IKOzFcfh28Ks7Cx&index=160&t=0s
To read more on pygame events, go to http://www.pygame.org/docs/ref/event.html
"""

import pygame
import time

pygame.init()  # To initialize the pygame module

# To decide on the color to use in the game window.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the game surface display with a param of 800 pixels by 600 pixels in a tuple, and assign the surface to var
# 'gameDisplay'.

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slither")

pygame.display.update()  # After changes has been set for a display, do a update.

gameExit = False

# The start location for the head of the snake.
lead_x = display_width / 2
lead_y = display_height / 2

lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

block_size = 10  # Setting the movement block size.
FPS = 30  # Setting the frame per secs.

font = pygame.font.SysFont(None, 25)


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])


while not gameExit:  # This means the gameExit value is still set at False.
    for event in pygame.event.get():  # Use the pygame's .event.get() method to get ALL events in the game window.
        if event.type == pygame.QUIT:  # If user clicks on close window button, then quit game and close the window.
            gameExit = True  # Then set the gameExit var value to True.
        if event.type == pygame.KEYDOWN:  # When detected any cursor key is pressed down,
            if event.key == pygame.K_LEFT:  # and left cursor key is pressed,
                lead_x_change = -block_size  # move to the left by 10 pixels,
                lead_y_change = 0  # maintain y-axis no change.
            elif event.key == pygame.K_RIGHT:  # When right cursor key is pressed,
                lead_x_change = block_size  # move to the right by 10 pixels.
                lead_y_change = 0  # maintain y-axis no change.
            elif event.key == pygame.K_UP:  # When up cursor key is pressed,
                lead_y_change = -block_size  # move up by 10 pixels,
                lead_x_change = 0  # maintain x-axis no change.
            elif event.key == pygame.K_DOWN:  # When down cursor key is pressed,
                lead_y_change = block_size  # move down by 10 pixels,
                lead_x_change = 0  # maintain x-axis no change.

    # Setting the boundaries on x and y axis to stop the game if snake goes out of the game window.
    if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
        gameExit = True

    lead_x += lead_x_change
    lead_y += lead_y_change

    # print(event)    # Print out ALL the keyboard and mouse happening in the game window onto the terminal console.

    gameDisplay.fill(white)  # Fill the background of the game window with white color.
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block_size, block_size])  # Draw a black rectangle with
    # [x-axis, y-axis, width, height].
    pygame.display.update()

    clock.tick(FPS)  # The speed at which the snake moves.

message_to_screen("You Lose", red)
pygame.display.update()
time.sleep(2)
pygame.quit()  # This is to stop the initializing of the pygame.
quit()
