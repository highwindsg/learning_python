#!/usr/bin/env python3

"""
It is possible to name the days 0 thru 6 where day 0 is Sunday and 
day 6 is Saturday. If you go on a wonderful holiday leaving on day 
number 3 (a Wednesday) and you return home after 10 nights. Write a 
general version of the program which asks for the starting day number, 
and the length of your stay, and it will tell you the number of day 
of the week you will return on.

eg.
0 - Sunday
1 - Monday
2 - Tuesday
3 - Wednesday
4 - Thursday
5 - Friday
6 - Saturday
"""

start_day = int(input("From 0-6, what day is it? "))
days_to_wait = int(input("How many days are you gone? "))
end_day = (start_day + days_to_wait) % 7

print(end_day)
