from sys import argv
from os.path import exists
import time

script, book1, book2 = argv

print(f"Copying content from {book1} to {book2}.")

in_file = open(book1)
indata = in_file.read()

print(f"The content from first book is {len(book1)} bytes long.")
print(f"And now checking if the new second book exists? {exists(book2)}")
time.sleep(3)
print("Ok new book exists, hit RETURN to continue or CTRL-C to abort the copying.")
input()

out_file = open(book2, 'w')
out_file.write(indata)

print("Ok, copying from book1 to book2 should be done now.")

in_file.close()
out_file.close()
