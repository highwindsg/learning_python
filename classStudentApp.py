#!/usr/bin/env python3

# File classStudent.py and classStudentApp.py are in the same dir.
# From classStudent, import the Student class.
from classStudent import Student

# Create a var obj 'student1' and set it to an instance of class
# Student() with four params.
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

# From student1 and student2 var, print out the name, gpa and major
# var obj.
print(student1.name, student1.gpa)
print(student2.name, student2.major)

