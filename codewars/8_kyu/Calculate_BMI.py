#!/usr/bin/env python3

"""
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""

def bmi(w, h):
    b = w / h ** 2
     
    if b <= 18.5:
        return "Underweight"
            
    elif b <= 25.0:
        return "Normal"
            
    elif b <= 30.0:
        return "Overweight"
            
    else:   # therefore any numbers greater than 30, will be obese.
        return "Obese"

"""
# Alternate clever solution

def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]


# Alternate lambda solution

bmi = lambda w,h: (lambda b=w/h**2: ["Underweight", "Normal", "Overweight", "Obese"][(18.5<b) + (25<b) + (30<b)])()

"""


print(bmi(50, 1.80))
print(bmi(80, 1.80))
print(bmi(90, 1.80))
print(bmi(110, 1.80))
print(bmi(50, 1.50))
    
print("")
