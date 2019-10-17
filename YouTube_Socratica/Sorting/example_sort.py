#!/usr/bin/env python3

# Alkaline earth metals.
# Create a list of earth metals.
earth_metals = ["Beryllium",
                "Magnesium",
                "Calcium",
                "Strontium",
                "Barium",
                "Radium"]

earth_metals.sort()
print(earth_metals)
print("")

earth_metals.sort(reverse=True)
print(earth_metals)
print("")

# Create a tuple of earth metals.
# Cannot use .sort() method on tuple as tuple are not changeable.
earth_metals = ("Beryllium",
                "Magnesum",
                "Calcium",
                "Strontium",
                "Barium",
                "Radium")

