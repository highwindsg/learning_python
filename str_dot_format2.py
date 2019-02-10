#!/usr/bin/env python3

# Creating a string from user input.

n1 = input("Enter a noun: ")
v = input("Enter a verb: ")
adj = input("Enter an adjective: ")
n2 = input("Enter a noun again: ")

statement = """The {} {} the {} {}
            """.format(n1, v, adj, n2)

print(statement)
