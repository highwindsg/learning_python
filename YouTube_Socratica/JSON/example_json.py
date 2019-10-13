#!/usr/bin/env python3

import json

print(dir(json))  # To see what are the available functions in json module.
print("")

# Use the 'json.load' func to load the txt file into proper JSON format.
json_file = open("///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/JSON/movie_1.txt",
                 "r", encoding="utf-8")
movie = json.load(json_file)
json_file.close()

print(movie)
print("")
print(type(movie))
print("")
print(movie["title"])
print("")
print(movie["actors"])
print("")
print(movie["release_year"])
print("")

# Use the 'json.loads' func in the data arrives in a form of a string, which is common in client-server applications.
# Once data is converted to json, null will be converted to None and false will be converted to False, the JSON format.
value = """
    {"title": "Tron: Legacy",
     "composer": "Daft Punk",
     "release_year": 2010,
     "budget": 170000000,
     "actors": null,
     "won_oscar": false
     }"""

tron = json.loads(value)
print(type(tron))
print("")
print(tron)
print("")

# To convert the 'movie' var from 'JSON format' into a proper 'JSON string format', use the 'json.dumps()' method.
print(movie)    # Shows in JSON format.
print(json.dumps(movie))    # Convert and shows in JSON strings format.
print(json.dumps(movie, ensure_ascii=False))  # The second param option will ensure that the cinematographer's name
# is preserved back in ASCII format.
