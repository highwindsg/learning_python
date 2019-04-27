#!/usr/bin/env python3

# Below program shows how to add two fractions
# by using the __add__ python add method.

class Fraction:     # Create a class named Fraction.

    def __init__(self, top, bottom):
        self.numerator = top
        self.denominator = bottom

    """
    Two fractions must have the same denominator to be added.
    Easiest way to make sure they have the same denominator
    is to simply use the product of the two denominators as a
    common denominator.
    """
    def __add__(self, otherfraction):
        newnum = self.numerator * otherfraction.denominator + \
                    self.denominator * otherfraction.numerator
        newden = self.denominator * otherfraction.denominator

        return Fraction(newnum, newden)

    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)

