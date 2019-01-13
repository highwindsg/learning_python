#!/usr/bin/env python3

# Convert a number score to a letter grade:
def letterGrade(score):
    if score >= 90:
        letter = "A"
    elif score >= 80:
        letter = "B"
    elif score >= 70:
        letter = "C"
    elif score >= 60:
        letter = "D"
    else:
        letter = "F"    # Fall through or default case
    return letter

scoreEn = int(input("Enter the score for English: "))
gradeEn = letterGrade(scoreEn)
scoreMath = int(input("Enter the score for Math: "))
gradeMath = letterGrade(scoreMath)
print("English grade is: ", gradeEn)
print("Math grade is: ", gradeMath)

#print(grade1)
#grade1 = letterGrade(75)
#print(grade2)
#print(letterGrade(95))      # Call and print in one statement
