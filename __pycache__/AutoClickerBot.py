#!/usr/bin/env python3

# https://www.youtube.com/watch?v=9KiqJXMpDXc

import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


delay = 0.01    # a hundred times a sec.
button = Button.left
start_stop_key = Keycode(char = "s")
exit_key = Keycode(char = "e")


class ClickMouse(threading.Thread):
    def ___init___(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        
    def start_clicking(self):
        self.running - True
        
    def stop_clicking(self):
        self.running = false
        
    def exit(self):
        self.stop_clicking()
        self.program_running = False
        
    def run(self):
        while self.program_running:
            while self.running():
                mouse.click(self.button)
                time.sleep(self.delay)
                
                
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
        
        
with Listener(on_press = on_press) as listener:
    listener.join()
    