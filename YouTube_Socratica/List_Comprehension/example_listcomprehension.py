#!/usr/bin/env python3

# Calculating the square of a number from 1 to 9.
squares = []    # Firstly, create a empty list and assign to var squares.

# Using a typical for loop.
for i in range(1, 10):
    squares.append(i**2)    # Use the .append() method and pass in the param to calculate the number to the power of 2.
print(squares)
print("")

# Using a for loop with list comprehension in a single line.
squares2 = [i**2 for i in range(1, 10)]
print(squares2)
print("")

# List comprehension with an 'if' clause.
# A list of movies and to find which movies that starts with letter G.
movies = ["Star Wars",
          "Gandhi",
          "Casablanca",
          "Shawshank Redemption",
          "Toy Story",
          "Gone with the Wind",
          "Citizen Kane",
          "It's a Wonderful Life",
          "The Wizard of Oz",
          "Gattaca",
          "Rear Window",
          "Ghostbusters",
          "To Kill A Mockingbird",
          "Good Will Hunting",
          "2001: A Space Odyssey",
          "Raiders of the Lost Ark",
          "Groundhog Day",
          "Close Encounters of the Third Kind"
          ]

gmovies = []    # Create an empty list and assign to var gmovies.
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print(gmovies)
print("")

# Now use list comprehension method.
gmovies = [title for title in movies if title.startswith("G")]
print(gmovies)
print("")

