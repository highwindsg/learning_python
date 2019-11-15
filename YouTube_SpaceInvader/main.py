#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=FfWpgLFMI7w&list=PLOgeKhf41meTmtKSF8IKOzFcfh28Ks7Cx&index=155&t=169s
https://github.com/attreyabhatt/Space-Invaders-Pygame/
"""

import pygame
import random
import math
from pygame import mixer  # Importing the sound mixer module from pygame library.

# Initialize the pygame
pygame.init()

# Set the game display windows with width(x-axis) of 800 and height(y-axis) of 600 pixels.
# Top left of the windows in (0, 0) and top right is (0, 800), bottom left is (0, 600) and bottom right is (800, 0)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.png")

# Background Sound
mixer.music.load("background.wav")  # Use the 'mixer.music' to load the music as the background music.
mixer.music.play(-1)  # '-1' is to play on loop continuously.

# Game window title and icon
pygame.display.set_caption("Space Invaders")

# For the window title, load the icon picture and assign to a var named 'icon'
icon = pygame.image.load("ufo.png")

# Use the pygame display .set_icon() method and pass in the icon var that contains the png file.
# This icon image is being displayed on the left side of the window title.
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
# playerImg = pygame.image.load("NicEr.png")
# Set the player's starting location axis.
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
# First set the value of enemy image, X & Y coordinates, speed changes to an empty list.
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5  # For this game, create 5 enemies.

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
#    enemyImg.append(pygame.image.load("LilianKeh.png"))
    # Set the enemy's starting location axis.
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)  # Set the movement pixel speed of the enemy on X-axis.
    enemyY_change.append(40)  # Set the downward pixel area when the enemy moves downward.

# Bullet
bulletImg = pygame.image.load("bullet.png")
# Set the enemy's starting location axis.
bulletX = 0
bulletY = 480  # Set the bullet firing Y-axis to be same as the player start position Y-axis.
bulletX_change = 0
bulletY_change = 20
bullet_state = "ready"  # 'ready' means you can't see the bullet on the screen. 'fire' means the bullet is currently
# moving.

# Score
score_value = 0  # Set the score value to 0 at start of game.
font = pygame.font.Font("Cream_Peach.ttf", 32)  # Pass in params for the filename of the font & pixel size of 32.

# X & Y coordinates of the score value text.
textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font("Cream_Peach.ttf", 64)  # Pass in params for the filename of the font & pixel size of 64.


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 255, 0))
    screen.blit(over_text, (200, 250))


def player(x, y):  # Create a func named 'player()' with x and y params.
    screen.blit(playerImg, (x, y))  # Use the .blit() method from screen to draw on on the surface of the game window.


def enemy(x, y, i):  # Create a func named 'enemy()' with x and y params.
    screen.blit(enemyImg[i], (x, y))  # Use the .blit() method from screen to draw on on the surface of the game window.


def fire_bullet(x, y):
    global bullet_state  # Set the 'bullet_state' var as a global var.
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Create a func named 'isCollision()' with four params.
"""The math formula can be learned from https://www.mathplanet.com/education/algebra-2/conic-sections/distance
-between-two-points-and-the-midpoint """


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True  # Set the var 'running' to True first so that the window stays open.

"""So if the close window is clicked, then change the value of var 'running' to False and close the game window."""
while running:
    # To set the bg color to black.
    # RGB - Red, Green, Blue and number does from 0 to 255. 0 is black.
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    """An 'event' is anything that happens within the game window. Eg. it may be a keystroke or mouse click."""
    for event in pygame.event.get():  # To get the state of the event in pygame using the .get() method.
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its left or right.
        if event.type == pygame.KEYDOWN:  # KEYDOWN means when you press down a key.
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
                playerX_change = 10
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound("laser.wav")  # From 'mixer' use the '.Sound()' method.
                    bullet_Sound.play()  # From 'mixer' use the '.Sound.play()' method without param.
                    # Get current X coordinate of the spaceship.
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:  # KEYUP means when you release a previously pressed key.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released")
                playerX_change = 0  # Setting value to 0 so that when keystroke is release, the spaceship will not move.

    # Checking for boundaries of spaceship so it doesn't go out of bound.
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # 736 is set because we need to offset 800 pixels width against 64 pixels of the spaceship.
        playerX = 736

    # Enemy movement.
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 8
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:  # 736 is set because we need to offset 800 pixels against 64 pixels of the spaceship.
            enemyX_change[i] = -8
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound("explosion.wav")  # From 'mixer' use the '.Sound()' method.
            explosion_Sound.play()  # From 'mixer' use the '.Sound.play()' method without param.
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)  # Client call the enemy() func so that it will appear after the screen appears.

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)  # Client call the player() func so that it will appear after the screen appears.
    show_score(textX, textY)
    pygame.display.update()  # Then update the display game window.
