#!/usr/bin/env python3

def computepay(h, r):

    shrs = float(40)    # Standard working hours.

    if h > shrs:
        xtra_hrs = h - shrs
        xtra_rates = float(r + (r / 2))
    Total_Pay = str(shrs * r + xtra_hrs * xtra_rates)

    return Total_Pay


hrs = input("Enter Hours:") # Hours worked.
h = float(hrs)
srates = input("Enter standard rates:")
r = float(srates)
p = computepay(h, r)
print("Pay", p)

