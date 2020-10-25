#!/usr/bin/env python3

"""
Ask the user for the time now (in hours 0 – 23), and ask for the number of hours to 
wait. Your program should output what the time will be on the clock when the alarm 
goes off.
"""

current_time = input("What is the current time (in hours eg. 0 - 23)?: ")
wait_time = input("How many hours do you want to wait?: ")

print(current_time)
print(wait_time)
total_time = int(current_time) + int(wait_time)
final_time = total_time % 24
print("The time after waiting is: ", final_time)
print("")
