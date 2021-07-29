#!/usr/bin/env python3

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
    
print("")

"""
Normally, once print has taken the content we passed and written it to the screen, then it 
writes a special character that creates a new line called the newline character. 
If we want print to write something else instead of the newline character, we use 
the end=" " parameter so that print continues for the current iterating loop.
"""



"""
We want to write a script that will output all possible team pairings. For this, the order 
of the names matters because for each game, the first name will be the home team and the 
second name is the away team. Of course, what we don't want to do is have a team playing 
against itself. So what statement do we need to use to avoid that?
What should the next line be to avoid both variables being printed with the same value?

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']

for home_team in teams:
    for away_team in teams:
"""

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:  # the condition is to ensure the names are different.
            print("[" + home_team + " vs " + away_team + "]")
    
print("")
