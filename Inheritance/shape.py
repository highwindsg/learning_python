#!/usr/bin/env python3

class Shape:        # Create a superclass named 'Shape'.
    __color = None  # Set a private var __color to None for now.
    
    def set_color(self, color):     # Define a func named set_color() with params self and color.
        self.__color = color        # From self, set the private var __color to color.
        
    def get_color(self):        # Define a func named get_color() with param self.
        return self.__color     # Return the value of the private var __color to the func get_color().
