#!/usr/bin/env python3

class Car:  # Create a class named Car.
    def __init__(self, speed, color):     # Define a init function with params 'self', 'speed' and 'color'.
        self.__speed = speed    # From self, set the attrib of __speed is to speed.
                                # Note that two underscore means the attrib is private and cannot be changed outside.
        self.__color = color    # From self, set the attrib of __color is to color.
                                # Note that two underscore means the attrib is private and cannot be changed outside.

    def set_speed(self, value):     # Define a func to set the speed with param 'self' and a 'value' of the speed.
        self.__speed = value      # From self, set the attrib of speed is to value.

    def get_speed(self):        # Define a func to get the speed with only param 'self',
        return self.__speed       # and just return the speed.
    
    def set_color(self, value):
        self.__color = value
    
    def get_color(self):
        return self.__color


ford = Car(200, "red")      # Set 'ford' as an instance of class Car, ford is-a Car,
                            # with params speed 200 and color red.
honda = Car(250, "blue")    # Set 'honda' as an instance of class Car, honda is-a Car,
                            # with params speed 250 and color blue.
audi = Car(300, "black")    # Set 'audi' as an instance of class Car, audi is-a Car,
                            # with params speed 300 and color black.

# ford.speed = 300            # Although it was set in line 17 for speed param to 200, we can still set
                            # a speed of 300 to the '.speed' param.

ford.set_speed(300)         # From 'ford', set the '.set_speed' attrib with param 300.

ford.__speed = 400          # This line will not work as we cannot change a private attrib outside of init func above.


print(ford.get_speed())     # Client call 'ford' and print the speed attrib.
print(ford.get_color())     # Client call 'ford' and print the color attrib.
