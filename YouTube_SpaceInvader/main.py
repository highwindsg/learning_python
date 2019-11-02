#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=FfWpgLFMI7w&list=PLOgeKhf41meTmtKSF8IKOzFcfh28Ks7Cx&index=155&t=169s
"""

import pygame

# Initialize the pygame
pygame.init()

# Set the game display windows with width(x-axis) of 800 and height(y-axis) of 600 pixels.
# Top left of the windows in (0, 0) and top right is (0, 800), bottom left is (0, 600) and bottom right is (800, 0)
screen = pygame.display.set_mode((800, 600))

# Game window title and icon
pygame.display.set_caption("Space Invaders")

# For the window title, load the icon picture and assign to a var named 'icon'
icon = pygame.image.load("ufo.png")
# Use the pygame display .set_icon() method and pass in the icon var that contains the png file.
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
# Set the player's starting location axis.
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
# Set the enemy's starting location axis.
enemyX = 370
enemyY = 50
enemyX_change = 0


def player(x, y):  # Create a func named 'player()' with x and y params.
    screen.blit(playerImg, (x, y))  # Use the .blit() method from screen to draw on on the surface of the game window.


def enemy(x, y):  # Create a func named 'enemy()' with x and y params.
    screen.blit(enemyImg, (x, y))  # Use the .blit() method from screen to draw on on the surface of the game window.


# Game loop
running = True  # Set the var 'running' to True first so that the window stays open.

"""So if the close window is clicked, then change the value of var 'running' to False and close the game window."""
while running:
    # To set the bg color to black.
    # RGB - Red, Green, Blue and number does from 0 to 255. 0 is black.
    screen.fill((0, 0, 0))

    """An 'event' is anything that happens within the game window. Eg. it may be a keystroke or mouse click."""
    for event in pygame.event.get():  # To get the state of the event in pygame using the .get() method.
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its left or right.
        if event.type == pygame.KEYDOWN:  # KEYDOWN means when you press down a key.
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                playerX_change = 5
        if event.type == pygame.KEYUP:  # KEYUP means when you release a previously pressed key.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")
                playerX_change = 0  # Setting value to 0 so that when keystroke is release, the spaceship will not move.

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # 736 is set because we need to offset 800 pixels width against 64 pixels of the spaceship.
        playerX = 736

    player(playerX, playerY)  # Client call the player() func so that it will appear after the screen appears.
    enemy(enemyX, enemyY)  # Client call the enemy() func so that it will appear after the screen appears.
    pygame.display.update()  # Then update the display game window.
