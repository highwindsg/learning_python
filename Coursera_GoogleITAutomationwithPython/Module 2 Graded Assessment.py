#!/usr/bin/env python3

"""
The color_translator function receives the name of a color, then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.
"""

def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    
    elif color == "green":
        hex_color = "#00ff00"
    
    elif color == "blue":
        hex_color = "#0000ff"
    
    else:
        hex_color = "unknown"
    
    return hex_color


print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown
print("")



"""
What's the value of this Python expression: "big" > "small"
"""

print("big" > "small")
print("")



"""
Students in a class receive their grades as Pass/Fail. 
Scores of 60 or more (out of 100) mean that the grade is "Pass". 
For lower scores, the grade is "Fail". 
In addition, scores above 95 (95 itself is not included) are graded as "Top Score". 
Fill in this function so that it returns the proper grade.
"""

def exam_grade(score):
    if score > 95:
        grade = "Top Score"
        
    elif score >= 60:
        grade = "Pass"
        
    else:
        grade = "Fail"
        
    return grade


print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail
print("")



"""
What's the value of this Python expression: 11 % 5?
"""

print(11 % 5)
print("")



"""
Complete the body of the format_name function. 
This function receives the first_name and last_name parameters and then returns a 
properly formatted string.

Specifically:

If both the last_name and the first_name parameters are supplied, the function should 
return like so:

print(format_name("Ella", "Fitzgerald"))
>>> Name: Fitzgerald, Ella

If only one name parameter is supplied (either the first name or the last name) ,the 
function should return like so:

print(format_name("Adele", ""))
>>> Name: Adele

or

print(format_name("", "Einstein"))
>>> Name: Einstein

Finally, if both names are blank, the function should return the empty string:
>>> 

"""

def format_name(first_name, last_name):
    # code goes here
    if len(first_name) > 0 and len(last_name) > 0:
        string = ("Name: " + last_name + ", " + first_name)
   
    elif len(first_name) == 0 and len(last_name) > 0:
        string = ("Name: " + last_name)
    
    elif len(first_name) > 0 and len(last_name) == 0:
        string = ("Name: " + first_name)
    
    else:
        string = ("")
    
    return string


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

print("")



"""
The longest_word function is used to compare 3 words. It should return the word with 
the most number of characters (and the first in the list when they have the same length). 
Fill in the blank to make this happen.
"""

def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word3):
        word = word1
  
    elif len(word2) >= len(word1) and len(word2) >= len(word3):
        word = word2
  
    else:
        word = word3
  
    return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))
print("")



"""
Output of the code below.
"""

def sum(x, y):
        return(x + y)
print(sum(sum(1, 2), sum(3, 4)))
print("")



"""
What's the value of this Python expression?
"""

print(((10 >= 5*2) and (10 <= 5*2)))
print("")



"""
The fractional_part function divides the numerator by the denominator, and returns just 
the fractional part (a number between 0 and 1). Complete the body of the function so that 
it returns the right number.
Note: Since division by 0 produces an error, if the denominator is 0, the function should 
return 0 instead of attempting the division.
"""

def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to keep just the 
    # fractional part of the quotient.
    if denominator > 0:
        return (numerator%denominator) / denominator
    return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
print("")