#!/usr/bin/env python3

# Create a dictionary of new york.
ny = {"locations":  # locations we use tuple as geo-coordinates never change, immutable.
      (40.7128, 74.0059),

      "celebs":     # celebrities we use list because list are mutable, can change.
      ["W. Allen",
       "Jay Z",
       "K. Bacon"],

      "facts":      # use dict, as is best for key-to-value of states-to-country names.
      {"state": "NY",
       "country": "America"
       }
      }

print(ny)
