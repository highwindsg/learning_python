#!/usr/bin/env python3

def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"


print(greet("en"), "Glenna")
print(greet("es"), "Sally")
print(greet("fr"), "Michael")
