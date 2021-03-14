#!/usr/bin/env python3


def eat(d):
    '''(dict of {str: int}) -> bool

    Each key in d is a fruit and each value is the quantity of that fruit.

    Return True if and only if any fuit was eaten.

    >>> eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
    True
    >>> eat({'apple': 0, 'banana': 0})
    False
    '''

    ate = False
    for fruit in d:
        if d[fruit] > 0:
            d[fruit] = d[fruit] - 1
            ate = True

    return ate


d = {'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1}

print(eat
      ({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
      )
print("")

print(eat
      ({'apple': 0, 'banana': 0})
      )
print("")

