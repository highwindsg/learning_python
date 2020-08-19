#!/usr/bin/env python3

"""
Below is an exmaple for 'tuple packing' the return values into a
tuple and return back to the func.
"""

def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r # Calculating circumference.
    a = 3.14159 * r * r # Calculating area.
    return c, a   # This will return the values to the func as tuples.
    # return (c, a) # The opening and closing parentheses are redundant.
    # return [c, a] # Can also use open and close sqaure brackets but
                    # also redundant.


print(circleInfo(10))
print("")


"""
It’s common to unpack the returned values into multiple variables.
"""

circumference, area = circleInfo(10)
print(circumference)
print(area)

circumference_two, area_two = circleInfo(45)
print(circumference_two)
print(area_two)
print("")


"""
Define a function called 'information' that takes as input, the
variables 'name', 'birth_year', 'fav_color', and 'hometown'.
It should return a tuple of these variables in this order.
"""

def information():
    name = input("Insert your name: ")
    birth_year = input("Insert your year of birth: ")
    fav_color = input("Insert your favourite color: ")
    hometown = input("Insert your hometown's name: ")
    return (name, birth_year, fav_color, hometown)

print(information())

# Alternatively:
# def information2(name, birth_year, fav_color, hometown):
#     return name, birth_year, fav_color, hometown

print("")


"""
Define a function called info with the following required
parameters: name, age, birth_year, year_in_college, and hometown.
The function should return a tuple that contains all the inputted
information.
"""

def info(name, age, birth_year, year_in_college, hometown):
    return name, age, birth_year, year_in_college, hometown

print(info("Tina", 20, 1996, "sophomore", "Detroit"))
print("")

