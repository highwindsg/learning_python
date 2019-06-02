#!/usr/bin/env python3

# Create a class named Student.
class Student:

    # Define a init func with params self and four others params.
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name    # From self, get the name attrib and set it to name.
        self.major = major  # From self, get the major attrib and set it to major.
        self.gpa = gpa      # From self, get the gpa and attrib and set it to gpa.
        self.is_on_probation = is_on_probation  # From self, get the is_on_probation
                                                # attrib and set it to is_on_probation.

"""
The above Student() class will be called by another file named classStudentApp.py
and will be used to print out the attribute of a student.
Therefore classStudent.py and classStudentApp.py needs to be in the same working dir.
"""
