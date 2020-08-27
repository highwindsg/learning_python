#!/usr/bin/env python3

# Func f with default param of 'a' and optional param of L=[].
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(f(4, ["Hello"]))
print(f(5, ["Greetings"]))
print("")
