fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)

# Use the '.startswith()' string method to select only those prefix we want.

# The script will produce extra blank lines in the output.
# This is due to the invisible newline character.
# Each of the lines ends with a newline, so the print
# statement prints the string in the variable 'line'
# which includes a newline and then print adds another
# newline, resulting in the double spacing effect we see.
