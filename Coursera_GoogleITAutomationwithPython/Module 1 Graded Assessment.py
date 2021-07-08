#!/usr/bin/env python3

"""
Keeping in mind there are 86400 seconds per day, write a program that calculates how many 
seconds there are in a week, if a week is 7 days.  Print the result on the screen.

Note: Your result should be in the format of just a number, not a sentence.
"""

secs_a_day = 86400
days_a_wk = 7
secs_in_a_week = days_a_wk * secs_a_day
print(secs_in_a_week)
print("")



"""
Use Python to calculate how many different passwords can be formed with 6 lower case 
English letters.  For a 1 letter password, there would be 26 possibilities.  
For a 2 letter password, each letter is independent of the other, so there would be 
26 times 26 possibilities.  Using this information, print the amount of possible 
passwords that can be formed with 6 letters.

hint:
As the alphabet length is 26, take a variable and assign 26 to it.
Take the length of the password from the user.
As it is given that each letter is independent from the other, repetitions are clearly allowed.
So, each block of n letter word can be filled with any of 26 letters i.e., 26 choices.
In such case, n blanks can be filled in 26x26x26x26x26x26....x26 ways. Simply in 26ⁿ ways.
As n=6, result will be 26⁶, which is equal to 308915776.
"""

pw_length = 6
alphabet_length = 26
pos_pws = 26**6
print(pos_pws)
print("")



"""
Most hard drives are divided into sectors of 512 bytes each.  
Our disk has a size of 16 GB. 
Fill in the blank to calculate how many sectors the disk has.
"""

disk_size = 16*1024*1024*1024
sector_size_each = 512
sector_amount = disk_size / sector_size_each
print(sector_amount)
print("")
