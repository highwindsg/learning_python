#!/usr/bin/env python3

class Car:  # Create a class named Car.
    pass    # 'pass' here means this is an empty class.
            # So you can set separate attributes below for the class.


# So 'ford', 'honda' and 'audi' are object.
ford = Car()    # Set 'ford' as an instance of class Car. ford is-a Car.
honda = Car()   # Set 'honda' as an instance of class Car. honda is-a Car.
audi = Car()    # Set 'audi' as an instance of class Car. audi is-a Car.

ford.speed = 200    # For 'ford', set the speed attrib to 200.
honda.speed = 220   # For 'honda', set the speed attrib to 220.
audi.speed = 250    # For 'audi', set the speed attrib to 250.

ford.color = "red"      # For 'ford', set the color attrib to red.
honda.color = "blue"    # For 'honda', set the color attrib to blue.
audi.color = "black"    # For 'audi', set the color attrib to black.


print(ford.speed)   # Client call 'ford' and print the speed attrib.
print(ford.color)   # Client call 'ford' and print the color attrib.
print("")


# Changing data attrib of obj.
ford.speed = 300
ford.color = "blue"


print(ford.speed)   # Client call 'ford' and print the newly changed speed attrib.
print(ford.color)   # Client call 'ford' and print the newly changed color attrib.
