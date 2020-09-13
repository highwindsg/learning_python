#!/usr/bin/env python3

L1 = [1, 7, 4, -2, 3]
L2 = ["Cherry", "Apple", "Blueberry"]


L1.sort()
print(L1)

print("----")

L2.sort()
print(L2)

print("")



""" Using sorted(obj) as a function, rather than a method and return
the sorted obj as a new list. This way the original obj will not be
changed. """

L2 = ["Cherry", "Apple", "Blueberry"]

L3 = sorted(L2)
print(L3)
print(sorted(L2))
print(L2)   # Unchanged.

print("----")

L2.sort()
print(L2)
print(L2.sort())    # Return value is None.

print("----")

print(sorted("Apple"))  # The string will be arranged in alphabetical
                        # order in a list.
print("")



"""
Write code to rearrange the strings in the list winners so that they 
are in alphabetical order by first name from A to Z.
"""

winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners = sorted(winners)
print(winners)
print("")



"""
Write code to switch the order of the winners list so that it is now 
Z to A, by first name. Assign this list to the variable z_winners.
"""

winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
z_winners = sorted(winners, reverse=True)
print(z_winners)
print("")



"""
The dictionary, medals, shows the medal count for six countries 
during the Rio Olympics. Sort the country names so they appear 
alphabetically. Save this list to the variable alphabetical.
"""

medals = {
    'Japan':41, 
    'Russia':56, 
    'South Korea':21, 
    'United States':121, 
    'Germany':42, 
    'China':70
    }

alphabetical = sorted(medals.keys())
print(alphabetical)
print("")
