#!/usr/bin/env python3

import csv
from datetime import datetime

print(dir(csv))  # To see what funcs and classes the module contains.
print("")

# google csv file downloaded from https://goo.gl/3zaUlD
path = "///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/CSV/google_stock_data.csv"

file = open(path, newline="")
""" open the file with params of the file path, with newline keyword for an empty
string. This is because some systems may end with a new line or carriage return or
even both. This newline keyword technique will ensure the module will work correctly
across all platforms. """

reader = csv.reader(file)  # From the csv module, use the .reader() func and pass 'file' as the param.

header = next(reader)  # As the first line of the csv file contains only header and no data, use the next() func
# to extract the first line out, and then we can read the data.

# data = [row for row in reader]  # Read the remaining data into var 'data'.

# The print out below will still produce string values only.
# print(header)
# print(data[0])
# print("")

# Converting the data to proper data type of datetime format, float and integers.
data = []  # First create a 'data' var with an empty list.
for row in reader:
    # row = [Date, Open, High, Low, Close, Volume, Adj. Close]
    date = datetime.strptime(row[0], "%m/%d/%Y")
    open_price = float(row[1])  # We use 'open_price' as the var name since 'open' itself is a Python builtin function.
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    # Add in the new vars into the empty 'data' list by appending.
    data.append([date, open_price, high, low, close, volume, adj_close])

# Client call to print out the data of the first line.
print(data[0])
print("")

"""Compute and store daily stock returns.
The file 'google_returns.csv' file will be created if it does not exist."""
returns_path = "///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/CSV/google_returns.csv"
file = open(returns_path, "w")  # Open the 'returns_path' var obj which has the csv filename, and assign to var 'file'.
writer = csv.writer(file)       # From the csv module, use the .writer() method with param of 'file' and assign to var
# 'writer'.
writer.writerow(["Date", "Return"])     # From var 'writer', use the .writerow() method and pass in the date and
# return row as a list.

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i + 1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price  # Formula for calculating daily return.
    formatted_date = todays_date.strftime("%m/%d/%Y")  # .strftime() means string format time.
    writer.writerow([formatted_date, daily_return])  # From 'writer' var obj, use the 'writerow()' and use the
    # formatted_date, and run the program.
