#!/usr/bin/env python3

# Create a list named scifi_authors with a list of science fiction authors.
scifi_authors = ["Isaac Asomov",
                 "Ray Bradbury",
                 "Robert Heinlein",
                 "Authus C. Clarke",
                 "Frank Herbert",
                 "Orson Scott Card",
                 "Douglas Adams",
                 "H. G. Wells",
                 "Leigh Brackett"]

# Sorting the science fiction authors names in alphabetical orders.
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)
