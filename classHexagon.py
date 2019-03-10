#!/usr/bin/env python3

# Create a Hexagon class with a method called calculate_perimeter that
# calculates and returns its perimeter.
# Then create a my_Hexagon object, and call the calculate_perimeter method
# on it, and print the result.
class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        sum_of_sides = self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6
        return sum_of_sides

my_Hexagon = Hexagon(1, 2, 3, 4, 5, 6)

print(my_Hexagon.calculate_perimeter())

