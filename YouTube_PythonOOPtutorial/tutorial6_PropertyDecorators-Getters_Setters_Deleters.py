#!/usr/bin/env python3

# Python Object-Oriented Programming
# https://www.youtube.com/watch?v=jCzT9XFZ5bw&pbjreload=10


class Employee:

	def __init__(self, first, last):  # Define a init constructor func with params self, first, last and pay.
		self.first = first  # From self, set a instance var of first and assign it to first.
		self.last = last  # From self, set a instance var of last and assign it to last.

	@property
	def email(self):  # Create a func named fullname with param self.
		return "{}.{}@email.com".format(self.first, self.last)

	@property
	def fullname(self):  # Create a func named fullname with param self.
		return "{} {}".format(self.first, self.last)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(" ")
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print("Delete Name!")
		self.first = None
		self.last = None


emp_1 = Employee("John", "Smith")

emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print("")

del emp_1.fullname
print(emp_1.fullname)

