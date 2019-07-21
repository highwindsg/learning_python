#!/usr/bin/env python3

def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello")

# Client call function greet() with param.
greet("en")
greet("fr")
greet("ch")
