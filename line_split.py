#!/usr/bin/env python3

line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

words = line.split()    # This line will split out the above line into a list of separated words.
print(words)
print("")

email = words[1]    # To get the email address only.
print(email)
print("")

pieces = email.split("@")   # Split the email address without the @ sign.
print(pieces)
print("")

print(pieces[1])    # Only print out the domain name, the second slice from var 'pieces'.
