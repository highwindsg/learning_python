#!/usr/bin/env python3

class Car:  # Create a class named Car.
    def __init__(self, speed, color):     # Define a init function with params 'self', 'speed' and 'color'.
        print(speed)            # Print out the param of 'speed'.
        print(color)            # Print out the param of 'color'.
        self.speed = speed      # From self, set the attrib of speed is to speed.
        self.color = color      # From self, set the attrib of speed is to speed.
        print("the __init__ is called")

#    pass    # 'pass' here means this is an empty class.
            # So you can set separate attributes below for the class.
            
# So 'ford', 'honda' and 'audi' are object.
ford = Car(200, "red")      # Set 'ford' as an instance of class Car, ford is-a Car,
                            # with params speed 200 and color red.
honda = Car(250, "blue")    # Set 'honda' as an instance of class Car, honda is-a Car,
                            # with params speed 250 and color blue.
audi = Car(300, "black")    # Set 'audi' as an instance of class Car, audi is-a Car,
                            # with params speed 300 and color black.
print("")
#
# ford.speed = 200    # For 'ford', set the speed attrib to 200.
# honda.speed = 220   # For 'honda', set the speed attrib to 220.
# audi.speed = 250    # For 'audi', set the speed attrib to 250.
#
# ford.color = "red"      # For 'ford', set the color attrib to red.
# honda.color = "blue"    # For 'honda', set the color attrib to blue.
# audi.color = "black"    # For 'audi', set the color attrib to black.
#
#
print(ford.speed)   # Client call 'ford' and print the speed attrib.
print(ford.color)   # Client call 'ford' and print the color attrib.
# print("")
#
#
# # Changing data attrib of obj.
# ford.speed = 300
# ford.color = "blue"
#
#
# print(ford.speed)   # Client call 'ford' and print the newly changed speed attrib.
# print(ford.color)   # Client call 'ford' and print the newly changed color attrib.
