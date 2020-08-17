#!/usr/bin/env python3

"""
Wherever python expects a single value, if multiple expressions
are provided, separated by commas, they are automatically packed
into a tuple. We can even omit the opening and closing parentheses
when assigning them to a single var, and python will still pack
them into a tuple.
"""

julia = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia"
print(julia)
print(type(julia))
print(julia[4])
print("")
print(julia[-1])
print("")


"""
Create a tuple called practice that has four elements:
‘y’, ‘h’, ‘z’, and ‘x’.
"""

practice = "y", "h", "z", "x"
print(practice)
print(type(practice))
print("")


"""
Provided is a list of tuples. Create another list called t_check
that contains the third element of every tuple.
"""

lst_tups = [('Articuno', 'Moltres', 'Zaptos'),
            ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'),
            ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'),
            ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'),
            ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'),
            ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')
            ]
print(lst_tups)
print("")

t_check = [lst_tups[0][2], lst_tups[1][2], lst_tups[2][2], lst_tups[3][2], lst_tups[4][2], lst_tups[5][2]]
print(t_check)
print("")


"""
Below, we have provided a list of tuples. Write a for loop that
saves the second element of each tuple into a list called seconds.
"""

tups = [('a', 'b', 'c'),
        (8, 7, 6, 5),
        ('blue', 'green', 'yellow', 'orange', 'red'),
        (5.6, 9.99, 2.5, 8.2),
        ('squirrel', 'chipmunk')
        ]
print(tups)
print("")

seconds = []    # Create an empty list as accumulator.
for tuple in tups:
    seconds = seconds + [tuple[1]]
print(seconds)
print("")
