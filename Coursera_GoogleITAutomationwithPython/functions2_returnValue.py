#!/usr/bin/env python3

def area_triangle(base, height):
    return base * height / 2


base = float(input("Enter base in cm: "))
height= float(input("Enter height in cm: "))


# Func call and assign returned value to var 'Ans'.
Ans = area_triangle(base, height)
print(Ans)
print("")



"""
Use the get_seconds function to work out the amount of seconds in 2 hours and 
30 minutes, then add this number to the amount of seconds in 45 minutes and 
15 seconds. Then print the result.
"""

def get_seconds(hours, minutes, seconds):
      return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)
print("")



"""
Convert total given seconds back into hours, mins and seconds.
// - this is a floor division operator. 
It divides a number and takes only the integer but not the remainder.
"""

def convert_seconds(seconds):
    hours = seconds // 3600 # calc how many hrs in a given amount of secs, because 1 hr equals to 3600 secs.
    minutes = (seconds - hours * 3600) // 60    # calc how many mins are left after subtracting the hrs.
    remaining_seconds = seconds - hours * 3600 - minutes * 60   # calc how many secs remain after subtracting mins.
    return hours, minutes, remaining_seconds


hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)
print("")
