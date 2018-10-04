fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if line.find("@uct.ac.za") == -1: continue
    print(line)

# Since 'find' looks for an occurrence of a string within another
# string and either returns the position of the string or -1 if the
# string was not found, we can write the above loop to 'find' lines
# that contains "@uct.ac.za".
