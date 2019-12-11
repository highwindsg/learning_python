#!/usr/bin/env python3

# Python Object-Oriented Programming
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM
# Create an empty class Employee().


class Employee:

	def __init__(self, first, last, pay):  # Define a init constructor func with params self, first, last and pay.
		self.first = first  # From self, set a instance var of first and assign it to first.
		self.last = last  # From self, set a instance var of last and assign it to last.
		self.pay = pay  # From self, set a instance var of pay and assign it to pay.
		self.email = first + "." + last + "@company.com"  # From self, set a new instance var of email and assign it with
	# var instance of first and last and domain name.

	def fullname(self):  # Create a func named fullname with param self.
		return "{} {}".format(self.first, self.last)


emp_1 = Employee("Corey", "Schafer", 50000)  # Set emp_1 to an instance of class Employee with params.
emp_2 = Employee("Test", "User", 60000)  # Set emp_2 to an instance of class Employee with params.

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())  # Print out the full name of emp_1 by calling the fullname() func method.
print("")

print(Employee.fullname(emp_1))  # Or can also print from the Employee class, use the fullname() func and pass in
# the var obj of emp_1.

