# 'Try' to 'open' the filename that user enters.
# And if the filename is wrong, then it is an 'exception'
# that the filename cannot be opened.
# Therefore we execute an 'exit()' function nicely.

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject lines in", fname)
