#!/usr/bin/env python3

# File classStudent2.py and classStudentApp2.py are in the same dir.
# From classStudent, import the Student class.
from classStudent2 import Student

# Create a var obj 'student1' and set it to an instance of class
# Student() with four params.
student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

print(student2.on_honor_roll())

