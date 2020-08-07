#!/usr/bin/env python3

opposites = {"up": "down", "right": "wrong", "true": "false"}
alias = opposites

print(alias is opposites)   # To check if alias is truly the same as opposites.

alias["right"] = "left"
print(opposites["right"])   # Print out the value of key 'right'.
print("")


mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}

# 'yourdict' is an alias mirror of 'mydict'.
yourdict = mydict

# This would also change the key value of elephant in 'mydict'.
yourdict["elephant"] = 999

print(mydict["elephant"])
print("")
