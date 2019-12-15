#!/usr/bin/env python3

# Python Object-Oriented Programming
# https://www.youtube.com/watch?v=3ohzBxoFHAY


class Employee:

	raise_amt = 1.04     # Setting a class var of raise_amount with a value of 1.04 or 4%.

	def __init__(self, first, last, pay):  # Define a init constructor func with params self, first, last and pay.
		self.first = first  # From self, set a instance var of first and assign it to first.
		self.last = last  # From self, set a instance var of last and assign it to last.
		self.pay = pay  # From self, set a instance var of pay and assign it to pay.
		self.email = first + "." + last + "@email.com"  # From self, set a new instance var of email and assign it with
	# var instance of first and last and domain name.

	def fullname(self):  # Create a func named fullname with param self.
		return "{} {}".format(self.first, self.last)

	def apply_raise(self):  # Create a func named apply_raise with param self.
		self.pay = int(self.pay * self.raise_amt)     # From self, set a instance var of pay and assign it to itself
	# and multiply by 4%.

	def __repr__(self):   # an unambiguous magic dunder representation method of the obj with param self.
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

	def __str__(self):    # a readable magic dunder representation string method of an obj with param self.
		return "{} - {}".format(self.fullname(), self.email)

	def __add__(self, other):   # Create a adding magic dunder method with params self which is on the left side, and
		# other which is on the right side of the equation.
		return self.pay + other.pay     # Adding the two employees pay obj together.


emp_1 = Employee("Corey", "Schafer", 50000)  # Set emp_1 to an instance of class Employee with params.
emp_2 = Employee("Test", "Employee", 60000)  # Set emp_2 to an instance of class Employee with params.

print(emp_1)
print("")

print(repr(emp_1))
print(str(emp_1))
print("")

print(emp_1.__repr__())
print(emp_1.__str__())
print("")

print(emp_1 + emp_2)
