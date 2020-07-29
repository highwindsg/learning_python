#!/usr/bin/env python3

opposites = {"up": "down", "right": "wrong", "true": "false"}
alias = opposites

print(alias is opposites)   # To check if alias is truly the same as opposites.

alias["right"] = "left"
print(opposites["right"])   # Print out the value of key 'right'.
