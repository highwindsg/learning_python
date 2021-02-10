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
