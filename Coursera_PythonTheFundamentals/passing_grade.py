#!/usr/bin/env python3

total = 0
grade_count = 0
grade1 = 0.0 
grade2 = 100.0 

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
else:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)



