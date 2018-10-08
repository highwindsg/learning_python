fhand = open("mbox-short.txt")

for line in fhand:
    line = line.rstrip()    # '.rstrip()' will remove trailing white spaces.
    if not line.startswith("From "):    # Only look for lines that starts with 'From '.
        continue                        # Else continue to ignore the other lines.
#    print(line)
    words = line.split()    # The split the line and assign it to the variable 'words'.
    print(words[2])         # Then take the 3rd index from the line in variable 'words'.
