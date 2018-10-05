# Asking the user to input the filename including the extension
# and place it in the variable 'fname' and open the file.

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
