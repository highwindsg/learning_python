#!/usr/bin/env python3

opposites = {"up": "down", "right": "wrong", "true": "false"}
alias = opposites

print(alias is opposites)

alias["right"] = "left"
print(opposites["right"])
