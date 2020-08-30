#!/usr/bin/env python3

initial = 7
def f(x, y = 3, z = initial):
    print("x, y, z are: " + str(x) + ", " + str(y) + ", " + str(z))

f(2)
f(2, z = 8) # Keyword arg must always be specified after a positional param.
f(x = 4, z = 8)
# Alternatively, keyword params allows us to put the keyword args
# in any particular order.
f(z = 8, x = 20)    # However param 'x' must to be specified as it
                    # is the required positional param in the func.

"""
Read python docs for more about keyword arguments.
https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments
"""

def parrot(voltage,
            state = "a stiff",
            action = "voom",
            type = "Norwegian Blue"):
    print("-- This parrot wouldn't", action, end = " ")
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)            # 1 positional arg
print("")
parrot(voltage = 1000)  # 1 keyword arg
print("")
parrot(voltage = 1000000, action = "VOOOOOM")   # 2 keyword args
print("")
parrot(action = "VOOOOOM", voltage = 1000000)   # 2 keyword args
print("")
parrot("a million", "bereft of life", "jump")   # 3 positional args
print("")
parrot("a thousand", state = "pushing up the daisies")  # 1 positional, 1 keyword arg
print("")


"""
Keyword Parameters with .format for interpolation of values.
"""

names_scores = [("Jack", [67, 89, 91]),
                ("Emily", [72, 95, 42]),
                ("Taylor", [83, 92, 86])
                ]

for name, scores in names_scores:
    print("The scores {name} got were: {s1}, {s2}, {s3}.".format(
    name = name,
    s1 = scores[0],
    s2 = scores[1],
    s3 = scores[2]))
print("")


"""
Keyword Parameters with .format to insert the same value into a
string multiple times by using {}s in the string everywhere you wnat
to interpolate them.
"""

# This works:
names = ["Jack", "Jill", "Mary"]
for n in names:
    print("'{}!' she yelled. '{}! {}, {}!'".format(n, n, n, "say hello"))
print("")

# And this also works:
names = ["Jack", "Jill", "Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n, "say hello"))
print("")


"""
What values will be printed below?
"""

names = ["Alexey", "Catalina", "Misuki", "Pablo"]
print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'"
.format(first = names[1], 
        f_one = names[0], 
        f_two = names[2], 
        f_three = names[3])
        )
print("")
