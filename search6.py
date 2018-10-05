# Asking the user to enter the filename (including the file extension)
# and pass it to the variable 'fname'.

fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject lines in", fname)
