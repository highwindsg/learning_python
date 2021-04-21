#!/usr/bin/env python3

# https://www.youtube.com/watch?v=DzQXk9jesPc

import pyautogui    # Import module 'pyautogui'.
import time # Import module 'time'.


pyautogui.FAILSAFE = False  # From pyautogui module, set the FAILSAFE attrib to False.
while True:
    time.sleep(15)  # From time module, set the a sleep timer to 15 secs.
    for i in range(0, 100): # For item in range 0-99,
        pyautogui.moveTo(0, i * 5)  # move mouse cursor.
