#!/usr/bin/env python3

# Python Object-Oriented Programming
# https://www.youtube.com/watch?v=BJ-VvGyQxho


class Employee:
	num_of_emps = 0  # Setting a class var of num_of_emps with a starting value of 0.
	raise_amount = 1.04  # Setting a class var of raise_amount with a value of 1.04 or 4%.

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
		self.pay = int(self.pay * self.raise_amount)  # From self, set a instance var of pay and assign it to itself
	# and multiply by 4%.

	@classmethod  # Create a class decorator or class method.
	def set_raise_amt(cls, amount):     # Define a func method set_raise_amt with params cls (cls is used to replace the
		# reserved keyword for class) and amount.
		cls.raise_amt = amount  # From cls var, set the raise_amt obj to the amount.


print("Number of employees before var emp_* are created = ", Employee.num_of_emps)
print("")

emp_1 = Employee("Corey", "Schafer", 50000)  # Set emp_1 to an instance of class Employee with params.
emp_2 = Employee("Test", "User", 60000)  # Set emp_2 to an instance of class Employee with params.

print("Number of employees after var emp_* are created = ", Employee.num_of_emps)
print("")

print(emp_1.__dict__)   # The __dict__ method will show the dictionary keys and values that emp_1 can return.
print(Employee.__dict__)    # This __dict__method line will show a raise_amount key and values from the Employee class
# as well as all the other func methods from the Employee class.

Employee.set_raise_amt(1.05)    # For the Employee class, create a set_raise_amt method with param of 1.05 or 5%.

print(Employee.raise_amt)  # Client call to print out the raise_amount class var from the Employee class.
print(emp_1.raise_amt)  # Client call to print out the local instance var of raise_amount of emp_1.
print(emp_2.raise_amt)  # Client call to print out the raise_amount of emp_2 from the Employee class, as there
# are no local instance of the raise_amount for emp_2.
print("")
