fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    # Skip "uninteresting lines" that does not starts with "From:".
    if not line.startswith("From:"):
        continue
    # Then continue to process the "interesting" line.
    print(line)

# The uninteresting lines are whose which do not start with "From:",
# which we skip using the 'continue' keyword.
# Therefore the script will only output lines that starts with "From:".
