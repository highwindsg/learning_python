#!/usr/bin/env python3


def mystery(s):
    i = 0
    result = ""

    while not s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result


print(mystery("123abc"))

