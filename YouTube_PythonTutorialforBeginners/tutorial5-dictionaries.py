#!/usr/bin/env python3

# https://www.youtube.com/watch?v=daefaLgNkw0

student = {
	"name": "John",
	"age": 25,
	"courses": ["Math", "CompSci"]
}

print(student)
# Using the .get() method and pass in the key as param will prevent a python error from stopping the program.
# This is a good practice to use the .get() method.
print(student.get("name"))
print(student.get("courses"))
print(student.get("country"))
print(student.get("state"))
print(student.get("age"))

