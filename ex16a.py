from sys import argv
import time 

script, booktitle = argv

print(f"We're going to erase the content in this {booktitle}.")
print("If you don't want that, hit CTRL-C (^C).")
print("But if you do indeed want to do that, hit RETURN.")

input("?")

print("Opening the book now and erasing the content.")
target = open(booktitle, 'w')

target.truncate()

print("Now please enter a new starting line for {booktitle}.")

line1 = input("line1: ")

print("Ready? I'm gonna start to write this line in now, so check back later.")
target.write(line1)
target.write("\n")
time.sleep(5)

print("And finally, we are done re-writing.")
target.close()

