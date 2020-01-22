#!/usr/bin/env python3

# https://www.youtube.com/watch?v=W8KRzm-HUcc&t=1247s

# List are mutable, can be changed.
list_1 = ["History", "Math", "Physics", "CompSci"]
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = "Art"
print(list_1)
print(list_2)

print("")


# Tuple are immutable, cannot be changed.
tuple_1 = ("History", "Math", "Physics", "CompSci")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = "Art"      # Tuple does not support item assignment, means it cannot be changed.
# print(tuple_1)      # Therefore will not be able to print out the lines below.
# print(tuple_2)

print("")


# Sets do not put items in order, and so the order of items may change. Sets uses curly-braces.
cs_courses = {"History", "Math", "Physics", "CompSci"}
art_courses = {"History", "Math", "Art", "Design"}

print(cs_courses)
print(art_courses)

print("Math" in cs_courses)
print("Design" in art_courses)

# To print out what are the common courses in cs and art courses, use the .intersection() method.
print(cs_courses.intersection(art_courses))     # From cs_courses, get the intersection() func and pass in the
# art_courses as param.

# To print out what are the courses in cs but not in art courses, use the .difference() method.
print(cs_courses.difference(art_courses))       # From cs_courses, get the difference() func and pass in the
# art_courses as param.

# To print out all the combined courses offered by both cs and art, use the .union() method.
print(cs_courses.union(art_courses))        # From cs_courses, get the .union() func and pass in the art_courses as
# param.

print("")


# Creating empty lists
empty_list = []
empty_list = list()


# Creating empty tuples
empty_tuple = ()
empty_tuple = tuple()


# Creating empty sets
# empty_set = {}  # This isn't right, it is a dict.
empty_set = set()   # To properly create a empty set, use the builtin set class eg. set(), with no values passed in.

