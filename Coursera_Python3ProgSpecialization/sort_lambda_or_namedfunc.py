#!/usr/bin/env python3

"""
When would it be better to use lambda expression and when to use a
named function?
Use lambda expression when the lambda expression can be short and
simple.
Use named function when it function gets too complex.
"""

"""
Each key is a state name and each value is a list of city names.
Sort the states based on their first city's shortest name to longest name.
"""

states = {
    "Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
    "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
    "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]
}

print(states)
print("")

# states[state] is the list of cities associated with a particular 
# state. So if state is a list of city strings, len(states[state][0]) 
# is the length of the first city name. So, we can use a lambda expression.
print(sorted(states, key=lambda state: len(states[state][0])))
print("")


"""
Find the number of cities in its city list that begin with a letter
'S', and sort that in order from least to most.
"""

# The function defining this property is harder to express using lambda 
# straightaway as it requires a filter and count accumulation pattern.
# So it is better to define a separate named function, and then parse
# the created named function into the lambda expression.
def s_cities_count(cities_list):
    # Return a count of how many cities begin with 'S'.
    ct = 0
    for city in cities_list:
        if city[0] == "S":
            ct += 1
    return ct

print(sorted(states, key=lambda state: s_cities_count(states[state])))
print("")



"""
Write code to switch the order of the winners list so that it is now 
A to Z by last name. Assign this list to the variable z_winners.
"""

winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']

z_winners = sorted(winners, key = lambda x: x.split()[-1])
print(z_winners)
print("")



"""
What how will the following data be sorted?
Ans: first city name (reverse alphabetically), then temperature (lowest to highest).
"""

weather = {'Reykjavik': {'temp':60, 'condition': 'rainy'},
           'Buenos Aires': {'temp': 55, 'condition': 'cloudy'},
           'Cairo': {'temp': 96, 'condition': 'sunny'},
           'Berlin': {'temp': 89, 'condition': 'sunny'},
           'Caloocan': {'temp': 78, 'condition': 'sunny'}}

sorted_weather = sorted(weather, key=lambda w: (w, -weather[w]['temp']), reverse=True)
print(sorted_weather)
print("")
