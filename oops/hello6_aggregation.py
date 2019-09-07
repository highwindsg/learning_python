#!/usr/bin/env python3

# Python aggregation

class Salary:   # Create a class named 'Salary'.
    def __init__(self, pay, bonus):     # Define a init start func with param self, pay and bonus.
        self.pay = pay                  # From 'self', set the '.pay' attrib is to 'pay'.
        self.bonus = bonus              # From 'self', set the '.bonus' attrib is to 'bonus'.

    def annual_salary(self):                    # Define a func named 'annual_salary' with param 'self'.
        return (self.pay * 12) + self.bonus     # Calc 12 mths pay plus bonus and return ans to the func.

class Employee:     # Create a class named 'Employee'.
    def __init__(self, name, age, salary):      # Define a func named init with param 'self' and three other params.
        self.name = name                        # From 'self', set the '.name' attrib is to 'name'.
        self.age = age                          # From 'self', set the '.age' attrib is to 'age.
        self.obj_salary = salary                #

    def total_salary(self):     # Define func named 'total_salary' with param 'self'.
        return self.obj_salary.annual_salary()  # From 'self.obj_salary', which is-a Salary() class, get the func
                                                # of 'annual_salary()', and return the calculated ans to the
                                                # total_salary() function.


salary = Salary(15000, 10000)       # Create a var obj of 'salary' is to the Salary() class and instantiate with
                                    # params of 15000 and 10000.
emp = Employee("Max", 25, salary)           # Client call the 'Employee()' class and pass in the values,
                                            # and assign to var 'emp'. Note that if 'emp' obj is deleted,
                                            # then the '.obj_salary' will also be deleted.
print(emp.total_salary())       # From 'emp' var obj, get the ans from the 'total_salary()' func.

"""
We have first created an instance of the salary class (line 25) and then we have parsed this instance into
the 'emp' constructor (line 27), which then can be used inside the 'Employee' class (in line 17).
This type of relationship is called 'aggregation'.
"""
