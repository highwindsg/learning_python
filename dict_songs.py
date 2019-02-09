#!/usr/bin/env python3

songs = {"Don't let me down": "The Chainsmokers",
         "With you": "Chris Brown",
         "Havana": "Camila Cabello",
         "Work from home": "Fifth Harmony"
         }

title = input("Type in the song name: ")

if title in songs:
    singer = songs[title]
    print(singer, "is the singer.")
else:
    print("Song is not available.")
