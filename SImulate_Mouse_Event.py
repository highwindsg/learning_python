#!/usr/bin/env python3

# https://www.youtube.com/watch?v=2BXr9U6ZL8Y

from pynput.mouse import Button, Controller
mouse = Controller()
mouse.position(1300, 900)
mouse.move(20, -13)
mouse.move(150, -130)
mouse.move(-150, 130)
mouse.click(Button.right, 1)
mouse.click(Button.left, 1)
mouse.click(Button.left, 1)
mouse.click(Button.left, 2)
mouse.release(Button.right)
mouse.release(Button.right)
mouse.scroll(0, -100)
