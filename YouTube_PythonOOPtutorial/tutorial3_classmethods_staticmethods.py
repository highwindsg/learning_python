#!/usr/bin/env python3

# https://www.youtube.com/watch?v=rq8cL2XMM5M


class Employee:
	num_of_emps = 0  # Setting a class var of num_of_emps with a starting value of 0.
	raise_amt = 1.04  # Setting a class var of raise_amount with a value of 1.04 or 4%.

	def __init__(self, first, last, pay):  # Define a init constructor func with params self, first, last and pay.
		self.first = first  # From self, set a instance var of first and assign it to first.
		self.last = last  # From self, set a instance var of last and assign it to last.
		self.pay = pay  # From self, set a instance var of pay and assign it to pay.
		self.email = first + "." + last + "@company.com"  # From self, set a new instance var of email and assign it with
		# var instance of first and last and domain name.

		Employee.num_of_emps += 1  # From the Employee class, instantiate a class var of num_of_emps to increase by 1.

	def fullname(self):  # Create a func named fullname with param self.
		return "{} {}".format(self.first, self.last)

	def apply_raise(self):  # Create a func named apply_raise with param self.
		self.pay = int(self.pay * self.raise_amt)  # From self, set a instance var of pay and assign it to itself
	# and multiply by 4%.

	@classmethod  # Adding a decorator named classmethod.
	def set_raise_amt(cls, amount):  # Define a func method named set_raise_amt with params cls and amount. cls is a
		# short form for class since class is a reserved word in Python.
		cls.raise_amt = amount  # For the cls param, set a raise_amt to the value of the amount param.

	@classmethod  # Adding an alternative classmethod.
	def from_string(cls, emp_str):  # Define a func from_string with params of the cls and emp_str.
		first, last, pay = emp_str.split(
			'-')  # Split the emp_str by '-' and pass the split value into the vars of first,
		# last and pay.
		return cls(first, last, pay)  # From the cls param, get the values from first, last and pay and return it to
	# the func from_string.

	@staticmethod  # Adding a staticmethod.
	def is_workday(
			day):  # Define a method is_workday with param day. Note that staticmethod does not requires the usual
		# self or cls params. So can just pass in a param that you need, since we want to find out when is the working day.
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		else:
			return True


emp_1 = Employee("Corey", "Schafer", 50000)  # Set emp_1 to an instance of class Employee with params.
emp_2 = Employee("Test", "User", 60000)  # Set emp_2 to an instance of class Employee with params.

import datetime
my_date = datetime.date(2016, 7, 10)

print("Is this a working day?", Employee.is_workday(my_date))     # To find out if the my_date passed in values is a
# working day or not.
print("")

Employee.set_raise_amt(1.05)  # Explicitly create a set_raise_amt method for the Employee class with param of 1.05
# or 5%. This will cause the printout result below from line 39 to 41 to show 1.05.

print(Employee.raise_amt)  # Client call to print out the raise_amount class var from the Employee class.
print(emp_1.raise_amt)  # Client call to print out the local instance var of raise_amount of emp_1.
print(emp_2.raise_amt)  # Client call to print out the raise_amount of emp_2 from the Employee class, as there
# are no local instance of the raise_amount for emp_2.
print("")

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp_1 = Employee.from_string(emp_str_1)  # From the Employee class, get the class method from_string, and pass in
# the values of var emp_str_1. Then assign it to new var new_emp_1.

print(new_emp_1.email)
print(new_emp_1.pay)
