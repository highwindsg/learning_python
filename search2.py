fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# We use the 'rstrip' method which strips whitespace from the
# right side of a string. This will give the output without the
# extra line spacing.
