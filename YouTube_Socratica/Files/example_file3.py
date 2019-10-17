#!/usr/bin/env python3

oceans = ["Pacific",
          "Atlantic",
          "Indian",
          "Southern",
          "Arctic"
          ]

# Open the file with 'w' write mode. And if the file exist, the content will be over-written.
with open("///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/oceans.txt", "w") as f:
    for ocean in oceans:
        #f.write(ocean)
        #f.write("\n")

        """Optionally can use the line below to replace line 12 and 13 so that the file will
        be written correctly the same way."""
        print(ocean, file=f)

# Open the file in 'a' append mode to add on to the file at the end.
with open("///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/oceans.txt", "a") as f:
    print(23*"-", file=f)
    print("These are the 5 oceans.", file=f)
