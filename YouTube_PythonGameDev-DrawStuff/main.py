#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=UHO2k-3sVcI
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


pygame.display.set_caption("Tanks")

# icon = pygame.image.load("apple.png")
# pygame.display.set_icon(icon)

# img = pygame.image.load("snakehead2.png")
# appleimg = pygame.image.load("apple.png")

clock = pygame.time.Clock()

# AppleThickness = 30     # The pixel size of apple is 30 by 30 pixels.
# block_size = 20  # Setting the movement block size.
FPS = 15  # Setting the frame per secs.

smallfont = pygame.font.SysFont("comicsanms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


def pause():

    paused = True
    message_to_screen("Paused",
                      black,
                      -100,
                      size="large")

    message_to_screen("Press C to continue or Q to quit.",
                      black,
                      25)

    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)   # 5 FPS


def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])


def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks",
                          green,
                          -100,
                          "large")

        message_to_screen("The objective is to shoot and destroy",
                          black,
                          -30)

        message_to_screen("the enemy tank before they destroy you.",
                          black,
                          10)

        message_to_screen("The more enemies you destroy, the harder they get.",
                          black,
                          50)

        message_to_screen("Press C to play, P to pause or Q to quit.",
                          black,
                          180)

        pygame.display.update()
        clock.tick(15)



def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15

    while not gameExit:  # This means the gameExit value is still set at False.

        if gameOver == True:
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")

            message_to_screen("Press C to play again or Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()


        while gameOver == True:

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
                    pass
                elif event.key == pygame.K_RIGHT:  # When right cursor key is pressed,
                    pass
                elif event.key == pygame.K_UP:  # When up cursor key is pressed,
                    pass
                elif event.key == pygame.K_DOWN:  # When down cursor key is pressed,
                    pass

                elif event.key == pygame.K_p:
                    pause()

        gameDisplay.fill(white)  # Fill the background of the game window with white color.
        pygame.display.update()
        clock.tick(FPS)  # The speed at which the snake moves.

    pygame.quit()  # This is to stop the initializing of the pygame.
    quit()


game_intro()
gameLoop()
