#!/usr/bin/env python3

# Converting a dictionary into a JSON formatted txt file and preserving the ASCII name format.

import json

# Create an empty dict and add in the keys and values below.
movie2 = {"title": "Minority Report", "director": "Steven Spielberg", "composer": "John Willians",
          "actors": ("Tom Cruise", "Colin Farrell", "Samantha Morton", "Max von Sydow"), "is_awesome": True,
          "budget": 102000000,
          "cinematographer": "Janus Kami\u0144ski"}

print(movie2)

# Open a new txt file if it does not exist, with write mode and utf-8 format, and assign to var 'file2'.
file2 = open("///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/JSON/movie_2.txt", "w",
             encoding="utf-8")
json.dump(movie2, file2, ensure_ascii=False)  # Use the json.dump() function and pass in params of the 'movie2' dict,
# var obj of the file to write into, and the option to use.
file2.close()   # Then close the file2 var obj.
