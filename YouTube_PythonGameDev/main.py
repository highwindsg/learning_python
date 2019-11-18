#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=K5F-aGDIYaM&list=PLOgeKhf41meTmtKSF8IKOzFcfh28Ks7Cx&index=160&t=0s
To read more on pygame events, go to http://www.pygame.org/docs/ref/event.html
"""

import pygame
import time
import random

pygame.init()  # To initialize the pygame module

# To decide on the color to use in the game window.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set the game surface display with a param of 800 pixels by 600 pixels in a tuple, and assign the surface to var
# 'gameDisplay'.

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slither")

img = pygame.image.load("snakehead2.png")

clock = pygame.time.Clock()

block_size = 20  # Setting the movement block size.
FPS = 15  # Setting the frame per secs.

font = pygame.font.SysFont(None, 25)


def snake(block_size, snakeList):

    gameDisplay.blit(img, (snakeList[-1][0], snakeList[-1][1]))

    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])  # Draw a black rectangle with
        # block_size to show the snake growing length.


def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color):
    textSurf, textRect = text_objects(msg, color)
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [display_width / 2, display_height / 2])
    textRect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    gameExit = False
    gameOver = False

    # The start location for the head of the snake.
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    # Rounding off the random range number is to align the snake and apple properly on the exact same axis.
    randAppleX = round(random.randrange(0, display_width - block_size)) #/ 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size)) #/ 10.0) * 10.0

    while not gameExit:  # This means the gameExit value is still set at False.

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():    # Use the pygame's .event.get() method to get ALL events in the game window.
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
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        # print(event)    # Print out ALL the keyboard and mouse happening in the game window onto the terminal console.

        gameDisplay.fill(white)  # Fill the background of the game window with white color.

        AppleThickness = 30
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)
        pygame.display.update()

#        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
#            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
#                randAppleX = round(random.randrange(0, display_width - block_size)) #/ 10.0) * 10.0
#                randAppleY = round(random.randrange(0, display_height - block_size)) #/ 10.0)* 10.0
#                snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleX and lead_y < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width - block_size))  # / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - block_size)) #/ 10.0)* 10.0
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX = round(random.randrange(0, display_width - block_size))  # / 10.0) * 10.0
                randAppleY = round(random.randrange(0, display_height - block_size)) #/ 10.0)* 10.0
                snakeLength += 1

        clock.tick(FPS)  # The speed at which the snake moves.

    pygame.quit()  # This is to stop the initializing of the pygame.
    quit()


gameLoop()
