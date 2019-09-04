#!/usr/bin/env python3

# Python aggregation.
# Delegating some responsibility from one class to another class.

class Salary:   # Create a class named 'Salary'.
    def __init__(self, pay, bonus):     # Define a init start func with param self, pay and bonus.
        self.pay = pay                  # From 'self', set the '.pay' attrib is to 'pay'.
        self.bonus = bonus              # From 'self', set the '.bonus' attrib is to 'bonus'.

    def annual_salary(self):                    # Define a func named 'annual_salary' with param 'self'.
        return (self.pay * 12) + self.bonus     # Calc 12 mths pay plus bonus and return ans to the func.

class Employee:     # Create a class named 'Employee'.
    def __init__(self, name, age, salary):  # Define a func named init with param 'self' and four other params.
        self.name = name                        # From 'self', set the '.name' attrib is to 'name'.
        self.age = age                          # From 'self', set the '.age' attrib is to 'age'.
        self.obj_salary = salary                # From 'self', set the '.obj_salary' attrib is to 'salary'.
        """ Therefore 'salary' in 'self.obj_salary' obj is the content, and the Employee() class
        is the container. Also can say the 'salary' is part-of the Employee class. """

    def total_salary(self):     # Define func named 'total_salary' with param 'self'.
        return self.obj_salary.annual_salary()  # From 'self.obj_salary', which is-a Salary() class, get the func
                                                # of 'annual_salary()', and return the calculated ans to the
                                                # total_salary() function.

salary = Salary(15000, 10000)   # Client call the 'Salary()' class and pass in the values, and assign to
                                # var 'salary'.
emp = Employee("Max", 25, salary)   # Client call the 'Employee()' class and pass in the values,
                                    # and assign to var 'emp'.
""" Therefore instead of using the 'salary' class inside the 'Employee()' class (line 18), we have first
created an instance of the 'salary' class (line 27) and we have passed this instance to the 'Employee()'
constructor (line 29) which can be used inside the 'Employee()' class (line 18).
And this type of relationship is called aggregation."""

print(emp.total_salary())       # From 'emp' var obj, get the ans from the 'total_salary()' func.
