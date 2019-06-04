#!/usr/bin/env python3

# Create a class named Student.
class Student:

    # Define a init func with params self and three others params.
    def __init__(self, name, major, gpa):
        self.name = name    # From self, get the name attrib and set it to name.
        self.major = major  # From self, get the major attrib and set it to major.
        self.gpa = gpa      # From self, get the gpa and attrib and set it to gpa.

    # Below is about creating an object function.
    # To create a honor roll function to check if the student with a certain GPA
    # can be granted the honor roll title.
    def on_honor_roll(self):    # Define a func named on_honor_roll with self param.
        if self.gpa >= 3.5:     # So if the student achieved a self GPA of greater
            return True         # or equal to 3.5, then it is TRUE that the student
        else:                   # has arcieved the honor roll.
            return False









"""
The above Student() class will be called by another file named classStudentApp2.py
and will be used to print out the attribute of a student.
Therefore classStudent.py and classStudentApp.py needs to be in the same working dir.
"""
