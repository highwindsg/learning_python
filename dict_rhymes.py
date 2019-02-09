#!/usr/bin/env python3

rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "live"
          }

num = input("Type a number:")
if num in rhymes:           #So if the number key exist in the rhymes dictionary then,
    rhyme = rhymes[num]     #assign the value of that key number to the var 'rhyme',
    print(rhyme)            #and print out the value of that key number.
else:
    print("Not found.")
