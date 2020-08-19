#!/usr/bin/env python3

julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"

print(type(julia))

"""
The number of var names on the left-hand side of the assignment
statement (line 16) must have the equal the number of values that
are on the right-hand side (line 3).

Unpacking a tuple on the right side and assigning them to 
vars on the left side.
"""

name, surname, birth_year, movie, movie_year, profession, birth_place = julia
print(name)
print(surname)
print(birth_year)
print(movie)
print(movie_year)
print(profession)
print(birth_place)

print("")

A, B, C, D = 1, 2, 3, 4
print(A)
print(B)
print(C)
print(D)

print("")

"""
With only one line of code, assign the variables water, fire,
electric, and grass to the values “Squirtle”, “Charmander”,
“Pikachu”, and “Bulbasaur”
"""

water, fire, electric, grass = "Squirtle", "Charmander", "Pikachu", "Bulbasaur"
print(water)
print(fire)
print(electric)
print(grass)

print("")

"""
With only one line of code, assign four variables, v1, v2, v3,
and v4, to the following four values: 1, 2, 3, 4.
"""

v1, v2, v3, v4 = 1, 2, 3, 4
print(v1)
print(v2)
print(v3)
print(v4)

print("")


"""
Passing a tuple to a function and have it automatically
unpacked the values into the parameter names.
"""

def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z))  # putting an '*' will unpack the tuple of var 'z'.
# print(add(z)) # this line causes an error as it is trying to add
                # a value of var z into the add() func, without
                # first unpacking the tuple (5, 4).

print("")

"""
Unpacking into iterator variables.
"""

d = {"k1": 3, "k2": 7, "k3": "some other value"}

for item in d.items():
    print("key: {}, value: {}".format(item[0], item[1]))
print("")

# Alternatively, would be better readable if use 'k' and 'v' as
# the iterable vars. So 'k' means key, and 'v' means value.

d2 = {"k1": 3, "k2": 7, "k3": "some other value"}

for k, v in d.items():
    print("key: {}, value: {}".format(k, v))
print("")

