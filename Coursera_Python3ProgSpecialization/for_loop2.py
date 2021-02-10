#!/usr/bin/env python3

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
Write a program that asks the user for the number of sides, the length of the side, 
the color, and the fill color of a regular polygon. The program should draw the 
polygon and then fill it in.
"""

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

num_sides = int(input("Enter the number of sides of the polygon: "))
length_sides = float(input("Enter the length of the side(cm): "))
colorname = input("Color of polygon? ")
fcolor = input("Fill color of polygon? ")

alex.color(colorname)
alex.fillcolor(fcolor)
alex.begin_fill()

for i in range(int(num_sides)):
    alex.forward(float(length_sides))
    alex.left(int(360 / num_sides))


alex.end_fill()
wn.exitonclick()
