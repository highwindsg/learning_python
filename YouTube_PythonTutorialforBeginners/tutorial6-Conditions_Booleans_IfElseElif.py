#!/usr/bin/env python3

# https://www.youtube.com/watch?v=DZwmZ8Usvnk

language = "Java"

if language == "Python":
	print("Language is Python")
elif language == "Java":
	print("Language is Java")
elif language == "JavaScript":
	print("Language is JavaScript")
else:
	print("No match")

print("")

# and
# or
# not
user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
	print("Admin Page")
else:
	print("Bad credentials")

if user == "Admin" or logged_in:
	print("Admin Page")
else:
	print("Bad credentials")

if not logged_in:
	print("Please log in")
else:
	print("Welcome")

