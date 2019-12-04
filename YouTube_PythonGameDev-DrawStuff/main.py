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

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)

clock = pygame.time.Clock()

# Set the game surface display with a param of 800 pixels by 600 pixels in a tuple, and assign the surface to var
# 'gameDisplay'.

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
tankWidth = 40
tankHeight = 20
turretwidth = 5
wheelWidth = 5

pygame.display.set_caption("Tanks")

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


def barrier(xlocation, randomHeight, barrier_width):

    pygame.draw.rect(gameDisplay, black, [xlocation, display_height - randomHeight, barrier_width, randomHeight])


def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])


def fireShell(xy, tankx, tanky, turPos):
    fire = True

    startingShell = list(xy)

    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print(startingShell[0], startingShell[1])
        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)

        startingShell[0] -= (10 - turPos) * 2

        # y = x ** 2
        startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015) ** 2) - (turPos + turPos / (12 - turPos)))

        if startingShell[1] > display_height:
            fire = False

        pygame.display.update()
        clock.tick(60)


def power(level):
    text = smallfont.render("Power: " + str(level) + "%", True, black)
    gameDisplay.blit(text, [display_width / 2, 0])


def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            # print(event)  # This will print out all events on mouse movement to terminal.
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

        # message_to_screen("Press C to play, P to pause or Q to quit.",
        #                  black,
        #                  180)

        cur = pygame.mouse.get_pos()

        button("play", 150, 500, 100, 50, green, light_green, action="play")
        button("controls", 350, 500, 100, 50, yellow, light_yellow, action="controls")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")

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


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight /2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def tank(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrents = [(x-27, y-2),
                        (x-26, y-5),
                        (x-25, y-8),
                        (x-23, y-12),
                        (x-20, y-14),
                        (x-18, y-15),
                        (x-15, y-17),
                        (x-13, y-19),
                        (x-11, y-21)
                        ]

    pygame.draw.circle(gameDisplay, black, (x, y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight))

    pygame.draw.line(gameDisplay, black, (x, y), possibleTurrents[turPos], turretwidth)

    pygame.draw.circle(gameDisplay, black, (x-15, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x-10, y+20), wheelWidth)

    pygame.draw.circle(gameDisplay, black, (x-15, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x-10, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x-5, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x+5, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x+10, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, black, (x+15, y+20), wheelWidth)

    return possibleTurrents[turPos]


def game_controls():

    gcont = True

    while gcont:
        for event in pygame.event.get():
            # print(event)  # This will print out all events on mouse movement to terminal.
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Controls",
                          green,
                          -100,
                          "large")

        message_to_screen("Fire: Spacebar",
                          black,
                          -30)

        message_to_screen("Move Turret: Up and Down arrows",
                          black,
                          10)

        message_to_screen("Move Tank: Left and Right arrows",
                          black,
                          50)

        message_to_screen("Pause: P",
                          black,
                          90)

        button("play", 150, 500, 100, 50, green, light_green, action="play")
        button("Main", 350, 500, 100, 50, yellow, light_yellow, action="main")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")

        pygame.display.update()
        clock.tick(15)


def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_controls()

            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15

    barrier_width = 50

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0

    currentTurPos = 0
    changeTur = 0

    fire_power = 50
    power_Change = 0

    xlocation = (display_width / 2) + random.randint(-0.2 * display_height, 0.2 * display_width)
    randomHeight = random.randrange(display_height * 0.1, display_height * 0.6)

    while not gameExit:  # This means the gameExit value is still set at False.
        gameDisplay.fill(white)  # Fill the background of the game window with white color.
        gun = tank(mainTankX, mainTankY, currentTurPos)

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
                    tankMove = -5

                elif event.key == pygame.K_RIGHT:  # When right cursor key is pressed,
                    tankMove = 5

                elif event.key == pygame.K_UP:  # When up cursor key is pressed,
                    changeTur = 1

                elif event.key == pygame.K_DOWN:  # When down cursor key is pressed,
                    changeTur = -1

                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_SPACE:
                    fireShell(gun, mainTankX, mainTankY, currentTurPos)

                elif event.key == pygame.K_a:
                    power_Change = -1

                elif event.key == pygame.K_d:
                    power_Change = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOLLAR:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_Change = 0

        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0

        if mainTankX - (tankWidth / 2) < xlocation + barrier_width:
            mainTankX += 5

        fire_power += power_Change

        power(fire_power)


        barrier(xlocation, randomHeight, barrier_width)
        pygame.display.update()
        clock.tick(FPS)  # The speed at which the snake moves.

    pygame.quit()  # This is to stop the initializing of the pygame.
    quit()


game_intro()
gameLoop()
