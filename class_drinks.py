#!/usr/bin/env python3

class DrinkingGlass:
    def SoftDrink(self):
        print("Coke")

    def LiquorDrink(self):
        print("Tequila")


Bartender = DrinkingGlass() # Set var Bartender to an instance of class DrinkingGlass.
Bartender.SoftDrink()       # From Bartender, get the attrib of SoftDrink, which
                            # is to print out the word 'Coke'.
Bartender.LiquorDrink()     # From Bartender, get the attrib of LiquorDrink, which
                            # is to print out the word 'Tequila'.
