#!/usr/bin/env python3

"""
Write one for loop to print out each character of the string my_str on a separate line.
"""

my_str = "MICHIGAN"

for c in my_str:
    print(c)
print("")



"""
In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are 
Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. 
Loop the output of these names in order.
"""

prefixes = "JKLMNOPQ"
suffix = "ack"

for item in prefixes:
    print(item + suffix)
print("")



"""
Get the user to enter some text and print it out in reverse order.
"""

EnText = input("Enter any text here: ")
print(EnText[::-1])
print("")



"""
Write a program that uses a for loop to print
One of the months of the year is January
One of the months of the year is February
One of the months of the year is March
etc …
"""

for amonth in [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]:
    print("One of the months of the year is", amonth)
print("")



"""
Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99 and 20.
Write a loop that prints each of the numbers on a new line.
Write a loop that prints each number and its square on a new line.
"""

num_list = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for item in num_list:
    print(item)
print("")

for item in num_list:
    print(item, item*item)
print("")



"""
Write a program that will go through a list of temperatures and print them out to the user.
"""

temperatures = [-3, 78, 95, 28, 56, 42, 56, 42, 56, 81, -10, -1]

for temp in temperatures:
    print("The weather outside is: " + str(temp))
print("")



"""
Write a program that will print out a greeting to each student in the list. 
This list should also keep track of how many students have been greeted and note that 
each time a new student has been greeted.
"""

students = ["Jay", "Stacy", "Iman", "Trisha", "Ahmed", "Daniel", "Shadae", "Tosin", "Charlotte"]
num_students = 0

for name in students:
    print("Welcome to class, " + name + ".")
    num_students += 1
    print(str(num_students) + "student(s) have entered the classroom.")
print("")



"""
Write one for loop to print out each element of the list 'several_things'. 
Then, write another for loop to print out the TYPE of each element of the list 'several_things'. 
To complete this problem you should have written two different for loops, 
each of which iterates over the list 'several_things', 
but each of those 2 for loops should have a different result.
"""

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for i in several_things:
    print(i)
print("")

for j in several_things:
    print(j, "is of", type(j))
print("")



"""
Write code that uses iteration to print out the length of each element of the list stored in 'str_list'.
"""

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]

for item in str_list:
    print(len(item))
print("")



"""
Write code to count the number of characters in original_str using the accumulation pattern and assign 
the answer to a variable num_chars. Do NOT use the len function to solve the problem (if you use it while 
you are working on this problem, comment it out afterward!)
"""

original_str = "The quick brown rhino jumped over the extremely lazy fox."

num_chars = 0

for c in original_str:
    num_chars += 1

print(num_chars)
print("")



"""
'addition_str' is a string with a list of numbers separated by the + sign. 
Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it 
to 'sum_val' (an integer). 
(You should use the .split("+") function to split by "+" and int() to cast to an integer).
"""

addition_str = "2+5+10+20"
addition_str_lst = addition_str.split("+")
print(addition_str_lst)
print(len(addition_str_lst))

for i in range(0, len(addition_str_lst)):
    addition_str_lst[i] = int(addition_str_lst[i])
    addition_int_lst = addition_str_lst # Just renaming the var 'addition_str_lst' to 'addition_int_lst'.
print(addition_int_lst)
    
sum_val = 0

for j in addition_int_lst:
    sum_val = sum_val + j
    j += 1
    
print("Sum of all the numbers is", sum_val)
print("")



"""
'week_temps_f' is a string with a list of fahrenheit temperatures separated by the , sign. Write code that 
uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it 
to 'avg_temp'. Do not hard code your answer (i.e., make your code compute both the sum or the number of 
items in 'week_temps_f') (You should use the .split(",") function to split by "," and float() to cast to a float).
"""

week_temps_f = "75.1, 77.7, 83.2, 82.5, 81.0, 79.5, 85.7"
week_temps_f_lst = week_temps_f.split(",")
print(week_temps_f_lst)
print(len(week_temps_f_lst))

for i in range(0, len(week_temps_f_lst)):
    week_temps_f_lst[i] = float(week_temps_f_lst[i])
    week_temps_f_float = week_temps_f_lst   # Just renaming the var 'week_temps_f_lst' to 'week_temps_f_float'.
print(week_temps_f_float)

sum_temp = 0

for j in week_temps_f_float:
    sum_temp = sum_temp + j
print(sum_temp)
avg_temp = sum_temp / len(week_temps_f_lst)
print(avg_temp)
print("")



"""
Write code to create a list of numbers from 0 to 67 and assign that list to the variable 'nums'. 
Do not hard code the list.
"""

nums = []

for i in range(0, 68):

    
print(nums)
print("")
