#!/usr/bin/env python3

# The .count() method requires that you provide one argument,
# which is what you would like to count.

print("Count")
print("=====")

a = "I have had an apple on my desk before 232!"
print(a.count("e")) # using the .count() method and parse in a 
# string to search for the count occurence.
print(a.count("ha"))
print(a.count("2"))
print("")


z = [
    "atoms",
    4,
    "neutron",
    6,
    "proton",
    4,
    "electron",
    4,
    "electron",
    "a",
    "atoms"
]
print(z.count("4"))
print(z.count(4))
print(z.count("a"))
print(z.count("electron"))
print("")
"""
Notice how “4” has a count of zero but 4 has a count of three? 
This is because the list z only contains the integer 4. There are 
never any strings that are 4. Additionally, when we check the count 
of “a”, we see that the program returns zero. Though some of the 
words in the list contain the letter “a”, the program is looking 
for items in the list that are just the letter “a”.
"""


# The .index() method can be helpful for both strings and lists and
# requires on argument.

print("Index")
print("=====")

music = "Pull out your music and dancing can begin"
bio = [
    "Metatarsal",
    "Metatarsal",
    "Fibula",
    [],
    "Tibia",
    "Tibia",
    43,
    "Femur",
    "Occipital",
    "Metatarsal"
]
print(music.index("m"))
print(music.index("your"))  # Will return the left most index of the argument.
print(bio.index("Metatarsal"))
print(bio.index("Fibula"))
print(bio.index([]))
print(bio.index(43))
print("")


seasons = [
    "winter",
    "spring",
    "summer",
    "fall"
]
# If it is unable to find the argument in the string or list, 
# then an error will occur.
print(seasons.index("autumn"))  # Error! As 'autumn' is not in the list.
print("")
