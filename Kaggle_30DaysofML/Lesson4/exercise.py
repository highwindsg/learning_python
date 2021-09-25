#!/usr/bin/env python3

def select_second(L):
    """Return the second element of the given list.
    If the list has no second element, return None.
    """
    if len(L) < 2:
        return None
    return L[1]


L = (3, 5)
#print(L)

print(
    select_second(L)
)
print("")



"""
You are analyzing sports teams. Members of each team are stored in a list. 
The Coach is the first name in the list, the captain is the second name in the list, 
and other players are listed after that. These lists are stored in another list, 
which starts with the best team and proceeds through the list to the worst team last. 
Complete the function below to select the captain of the worst team.
"""

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd
    player (captain) from the last listed team.
    """
    return teams[-1][1]



"""
The next iteration of Mario Kart will feature an extra-infuriating new item, the 
Purple Shell. When used, it warps the last place racer into first place and the 
first place racer into last place. Complete the function below to implement the 
Purple Shell's effect.
"""

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list)
    to the last place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    
    # One way to do the swap is x[0], x[-1] = x[-1], x[0].
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp
    return


r = ["Mario", "Bowser", "Luigi"]
purple_shell(r)
print(r)
print("")
