#!/usr/bin/env python3

"""
Read in the contents of the file SP500.txt which has monthly data
for 2016 and 2017 about the S&P 500 closing prices as well as some
other financial indicators, including the “Long Term Interest
Rate”, which is interest rate paid on 10-year U.S. government
bonds.
Write a program that computes the average closing price (the
second column, labeled SP500) and the highest long-term interest
rate. Both should be computed only for the period from June 2016
through May 2017. Save the results in the variables mean_SP and
max_interest."""

f = open("SP500.txt", "r")
line = f.readlines()
sum = 0
lst = []
for lin in line[6:18]:
    lin = lin.split(",")
    sum += float(lin[1])
    lst += [lin[5]]

mean_SP = sum/12
print(mean_SP)

big = lst[0]
for i in range(len(lst)):
    if lst[i]>big:
        big = lst[i]
max_interest = float(big)
print(max_interest)

"""
Explanation:
first open the .txt file to read
then use readline to read all the lines in the .txt file.
since we have to find the mean_SP let's first take the sum and
later divide it by 12.
initialize an empty string lst
open the for loop to read the data from 6/1/16 to 5/1/17
divide the lin in the form of a list using .split
find sum of all the SP500 values
start adding the value of 6th element from lin in the string lst
mean_SP = sum/12 (june - may =12 months)
print mean_SP
initialize the first element of lst to big, assuming that it is
the biggest interest rate among all
open the loop starting fron i=0 to i= length of string lst
check if big is greater than rest of the values present in lst
if no then replace the value of big by the greater digit
since all the elements in lst are in the form of a string so
convert them into float variable and assign its value to
max_interest
print max_interest

Read more on Brainly.in - https://brainly.in/question/16482948#readmore
"""

