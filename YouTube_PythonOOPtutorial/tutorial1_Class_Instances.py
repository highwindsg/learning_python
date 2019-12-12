#!/usr/bin/env python3

# Python Object-Oriented Programming
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM
# Create an empty class Employee().


class Employee:

	num_of_emps = 0     # Setting a class var of num_of_emps with a starting value of 0.
	raise_amount = 1.04     # Setting a class var of raise_amount with a value of 1.04 or 4%.

	def __init__(self, first, last, pay):  # Define a init constructor func with params self, first, last and pay.
		self.first = first  # From self, set a instance var of first and assign it to first.
		self.last = last  # From self, set a instance var of last and assign it to last.
		self.pay = pay  # From self, set a instance var of pay and assign it to pay.
		self.email = first + "." + last + "@company.com"  # From self, set a new instance var of email and assign it with
	# var instance of first and last and domain name.

		Employee.num_of_emps += 1   # From the Employee class, instantiate a class var of num_of_emps to increase by 1.

	def fullname(self):  # Create a func named fullname with param self.
		return "{} {}".format(self.first, self.last)

	def apply_raise(self):  # Create a func named apply_raise with param self.
		self.pay = int(self.pay * self.raise_amount)     # From self, set a instance var of pay and assign it to itself
	# and multiply by 4%.


emp_1 = Employee("Corey", "Schafer", 50000)  # Set emp_1 to an instance of class Employee with params.
emp_2 = Employee("Test", "User", 60000)  # Set emp_2 to an instance of class Employee with params.

print("emp_1's email address is", emp_1.email)
print("emp_2's email address is", emp_2.email)

print("emp_1's full name is", emp_1.fullname() + ".")  # Print out the full name of emp_1 by calling the fullname()
# func method.
print("emp_1's full name is", Employee.fullname(emp_1) + ".")  # Or can also print from the Employee class, use the
# fullname() func and pass in the var obj of emp_1.
print("")

print(emp_1.pay)    # Print out emp_1's pay.
emp_1.apply_raise()     # Apply the raise of 4% on emp_1's pay.
print(emp_1.pay)    # Print out emp_1's pay after adding 4%.
print("")

emp_1.raise_amount = 1.05   # Setting a local instance var attrib of raise_amount for emp_1 with a value of 1.05 or 5%.

print(Employee.raise_amount)    # Client call to print out the raise_amount class var from the Employee class.
print(emp_1.raise_amount)       # Client call to print out the local instance var of raise_amount of emp_1.
print(emp_2.raise_amount)       # Client call to print out the raise_amount of emp_2 from the Employee class, as there
# are no local instance of the raise_amount for emp_2.
print("")

print(Employee.num_of_emps)     # Client call to print out the class var of num_of_emps from the Employee class.
# In line 30 and 31, when var emp_1 and emp_2 are created and takes on the Employee class and params, the num_of_emps
# are then created, or instantiated.
