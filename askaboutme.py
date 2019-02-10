#!/usr/bin/env python3

# Create a dict that contains different attributes about yourself, and returns
# the result from the dict you created.

me = {
    "name": "Caven",
    "height": "1.78m",
    "fav_color": "Red",
    "fav_author": "JRR Tokien",
    }

question = input("What would you like to know [name,height,fav_color,fav_author]: ")

if question in me:
    answer = me[question]
    print(answer)
else:
    print("Not found, please try again.")
